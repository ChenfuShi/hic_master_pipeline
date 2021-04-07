########################################
# script for merging all valid pairs files



########################################

import os
import logging
import subprocess


def merge_validpairs(Configuration, inputs):
    """take inputs and cat into a merged valid pairs file"""
    logging.info("Merging valid pairs files")
    logging.info(inputs)
    merged_outdir = os.path.join(Configuration.merged_validpairs,Configuration.merged_output,Configuration.merged_output)
    os.makedirs(merged_outdir, exist_ok=True)

    input_files = []
    for i in inputs:
        ls_dir = os.listdir(os.path.join(Configuration.HiC_pro_outs_dir,i,"hic_results","data",i))
        input_files.append([x for x in ls_dir if "allValidPairs" in x][0]) # assume that there is only one file with this format
    check_compressed = [x.endswith(".gz") for x in input_files]
    comb_inputs = " ".join(input_files)
    if all(check_compressed): 
        output_file = os.path.join(merged_outdir, Configuration.merged_output + ".allValidPairs.gz")
    elif not any(check_compressed):
        output_file = os.path.join(merged_outdir, Configuration.merged_output + ".allValidPairs")
    else:
        raise Exception("Not all files were either compressed or uncompressed!")

    with open(output_file, "w") as combined_output:
        subprocess.run(f"cat {comb_inputs}",shell=True,stdout=combined_output, cwd = Configuration.merged_validpairs)
    logging.info("Merging valid pairs files finished")

    # no need to uncompress anymore because updated hicpro2juicebox.sh
    # proc = subprocess.run("gunzip" +  Configuration.merged_output + ".allValidPairs.gz", shell=True, cwd = merged_outdir)
    # output_file = os.path.join(merged_outdir, Configuration.merged_output + ".allValidPairs")
    # logging.info("uncompressed final file")
    return output_file

