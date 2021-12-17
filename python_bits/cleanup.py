########################################
# script for cleaning up at the end



########################################

import os
import logging
import subprocess
import string
import random


def cleanup(Configuration, obj = "normal"):
    logging.info(f"compressing un-needed files")
    if obj == "normal":
        hic_pro_output = os.path.join(Configuration.HiC_pro_outs_dir, Configuration.file_to_process, "hic_results")
        matrix_loc = os.path.join(hic_pro_output, "matrix")
        data_loc = os.path.join(hic_pro_output, "data")
        proc = subprocess.run("find -L ./ -maxdepth 6 -type f ! -name '*.gz' -print0 | xargs -L1 -P8 -0 gzip",shell=True, cwd = matrix_loc)
        proc = subprocess.run("find -L ./ -maxdepth 6 -type f ! -name '*.gz' -print0 | xargs -L1 -P8 -0 gzip",shell=True, cwd = data_loc)

        logging.info(f"Hi-C pro files compressed")
    elif obj == "merging":
        merged_outdir = os.path.join(Configuration.merged_sparsemat,Configuration.merged_output)
        matrix_loc = os.path.join(merged_outdir, "matrix")
        proc = subprocess.run("find -L ./ -maxdepth 6 -type f ! -name '*.gz' -print0 | xargs -L1 -P8 -0 gzip",shell=True, cwd = matrix_loc)
        logging.info(f"Hi-C pro matrix files compressed")