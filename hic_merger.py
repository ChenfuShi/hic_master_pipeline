########################################
# script to merge allvalidpairs and create a juicebox file for merged. 
# then calls hicpro as well to call matrix and do ontad and compartments
########################################

from python_bits.config import Config
import os
from random import random
from time import sleep
import argparse
import logging
from python_bits import merging, hic_pro, compartments, matrix_ontad, cleanup



if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Merge results from individual analysis.')

    parser.add_argument('-i','--inputs', dest="inputs", action='append', 
                        help='call multiple times for each file you want to merge', required=True)
    parser.add_argument('-o','--output', dest="output", action='store', 
                        help='name of the output file', required=True)                  
    parser.add_argument("-s",'--steps', dest='step', action='append', required=False,
                        help='chose steps instead of running everything. Currently not implemented')

	# parse arguments
    args = parser.parse_args()

    # set up configuration object for all steps. this sets up logging as well
    Configuration = Config()

    Configuration.merged_output = args.output
    # check if we can find all folders that we need
    Configuration.file_to_process = args.output

    known_files = os.listdir(Configuration.HiC_pro_outs_dir)

    test_files = args.inputs

    if len(test_files) < 2:
        logging.error("There were less than 2 files in the input")
        raise Exception

    for n in test_files:
        if n not in known_files:
            logging.error(f"Sample {n} not found in HiC-Pro outputs")
            raise Exception

    # merge the valid pairs
    merged_validpairs = merging.merge_validpairs(Configuration, test_files)

    # run juicebox to create the merged hic file
    hic_pro.run_juicebox(Configuration, merged_validpairs)
    
    # get compartments
    compartments.call_compartments(Configuration)

    # create sparse matrixes from valid pair file
    hic_pro.make_merged_matrixes(Configuration)

    # run matrixes
    Configuration.HiC_pro_outs_dir = Configuration.merged_sparsemat
    matrix_ontad.generate_mat_ontad(Configuration)

    # compress hi-c pro stuff
    cleanup.cleanup(Configuration, obj = "merging")