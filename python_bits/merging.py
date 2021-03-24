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
        input_files.append(os.path.join(Configuration.HiC_pro_outs_dir,i,"hic_results","data",i,i+".allValidPairs"))
    comb_inputs = " ".join(input_files)

    output_file = os.path.join(merged_outdir, Configuration.merged_output + ".allValidPairs")
    with open(output_file, "w") as combined_output:
        subprocess.run(f"cat {comb_inputs}",shell=True,stdout=combined_output, cwd = Configuration.merged_validpairs)
    logging.info("Merging valid pairs files finished")
    return output_file

