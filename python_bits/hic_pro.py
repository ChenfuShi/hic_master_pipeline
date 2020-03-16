########################################
# script for running hic-pro



########################################

import os
import logging
import subprocess
from collections import defaultdict
import string
import random

def run_hic_pro(Configuration):
    """runs hic pro"""

    configuration_file = _get_protocol(Configuration)

    trimmed_files = os.path.join(Configuration.Trimmed_dir,Configuration.file_to_process) # this will have a directory in it containing the files
    temp_loc = os.path.join(Configuration.HiC_pro_temp_dir, Configuration.file_to_process)
    final_loc = os.path.join(Configuration.HiC_pro_outs_dir, Configuration.file_to_process)
    logging.info("Running HiC_pro to temporary directory")
    proc = subprocess.run([Configuration.HiC_pro_loc,"-i",trimmed_files,
        "-o", temp_loc, "-c",configuration_file])

    logging.info("HiC-pro finished, now copying files over to output directory. This drops the BAM files")
    proc = subprocess.run("rm -r " + temp_loc+"/bowtie_results/bwt2_*",shell=True)
    proc = subprocess.run("rm " + temp_loc+"/bowtie_results/bwt2/*/*.bam",shell=True)
    proc = subprocess.run(["mv",temp_loc,final_loc])
    logging.info("HiC-pro step done and files moved to output directory")


def run_juicebox(Configuration,overwrite_hic = None):
    """runs juicebox converter"""
    logging.info("Converting HiC-pro output to juicebox format")
    random_string =''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    hic_pro_output_file = os.path.join(Configuration.HiC_pro_outs_dir, Configuration.file_to_process,"hic_results","data",Configuration.file_to_process,Configuration.file_to_process+".allValidPairs")
    if overwrite_hic:
        hic_pro_output_file = overwrite_hic
    juicebox_output = os.path.join(Configuration.Juicebox_dir, Configuration.file_to_process)
    os.makedirs(juicebox_output,exist_ok=True)
    proc = subprocess.run([Configuration.hicpro2juicebox_loc,"-j",Configuration.juicer_tools_loc,
        "-i",hic_pro_output_file,"-t",os.path.join(Configuration.HiC_pro_temp_dir,random_string),"-g","hg38"],cwd = juicebox_output)
    logging.info("Conversion finished")

    
def make_merged_matrixes(Configuration):
    """utility to merge matrixes, put here because needed some stuff here"""
    logging.info("running contact matrix building with merged valid pairs")
    merged_indir = os.path.join(Configuration.merged_validpairs,Configuration.merged_output)
    merged_outdir = os.path.join(Configuration.merged_sparsemat,Configuration.merged_output)
    configuration_file = _get_protocol(Configuration)

    proc = subprocess.run([Configuration.HiC_pro_loc,"-i",merged_indir,
        "-o", merged_outdir, "-c",configuration_file, "-s", "build_contact_maps", "-s", "ice_norm"])
    logging.info("sparse matrixes build done")




def _get_protocol(Configuration):
    protocol = Configuration.file_to_process.split("_")[-1]

    if protocol == "HIND":
        return Configuration.HiC_pro_HIND
    elif protocol == "MBOI":
        return Configuration.HiC_pro_MBOI
    elif protocol == "ARIMA":
        return Configuration.HiC_pro_ARIMA
    else:
        logging.error("Couldn't identify the protocol, please check name of folder")
        raise Exception
