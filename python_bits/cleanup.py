########################################
# script for cleaning up at the end



########################################

import os
import logging
import subprocess
import string
import random


def cleanup(Configuration):
    logging.info(f"compressing un-needed files")

    hic_pro_output = os.path.join(Configuration.HiC_pro_outs_dir, Configuration.file_to_process, "hic_results")
    matrix_loc = os.path.join(hic_pro_output, "matrix")
    data_loc = os.path.join(hic_pro_output, "data")
    proc = subprocess.run("find -L ./ -maxdepth 6 -type f ! -name '*.gz' -print0 | xargs -L1 -P8 -0 gzip",shell=True, cwd = matrix_loc)
    proc = subprocess.run("find -L ./ -maxdepth 6 -type f ! -name '*.gz' -print0 | xargs -L1 -P8 -0 gzip",shell=True, cwd = data_loc)

    logging.info(f"Hi-C pro files compressed")