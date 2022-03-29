########################################
# script for converting a hic file to mcool
# doing it this way because should be the same compared to running it from hic-pro


########################################

import os
import logging
import subprocess
from collections import defaultdict
import string
import random
from python_bits.helpers import clean_dir
import shutil

def hic2cool(Configuration):
    hic_file = os.path.join(Configuration.Juicebox_dir, Configuration.file_to_process, Configuration.file_to_process + ".allValidPairs.hic")
    output_file = os.path.join(Configuration.cool_dir, Configuration.file_to_process)
    subprocess.run(["hic2cool", "convert", hic_file, output_file, "-p", "6"])
