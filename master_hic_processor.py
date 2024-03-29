########################################
# main script that calls all functions

# naming system:
# folder name needs to be sampleName_PROTOCOL
# within the folder name needs to be id+lane_R1.fastq.gz and R2

#protocols needs to be HIND MBOI or ARIMA
########################################

from python_bits.config import Config
import os
from random import random
from time import sleep
import argparse
import logging
from python_bits import trimming, hic_pro, matrix_ontad, compartments, cleanup, convert_hic2cool


if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Wrapper function for all steps of Hi-C analysis')

    parser.add_argument("-i",'--input', dest='infile', action='store', required=False,
                        help='input folder to force. Will overwrite all ouputs')
    parser.add_argument("-s",'--steps', dest='step', action='append', required=False,
                        help='chose steps instead of running everything')

	# parse arguments
    args = parser.parse_args()

    # set up configuration object for all steps. this sets up logging as well
    Configuration = Config()


    if args.infile == None:
        all_raws_present = os.listdir(Configuration.RAW_input_dir)

        all_processed = os.listdir(Configuration.TADs_dir)
        # chose the first one of the ones that are still not processed and run 
        for i in all_raws_present:
            if i not in all_processed:
                os.makedirs(os.path.join(Configuration.TADs_dir,i),exist_ok=True)
                Configuration.file_to_process = i
                break

        if Configuration.file_to_process == None:
            logging.error("There were no new files to process")
            raise Exception
        
    else:
        Configuration.file_to_process = args.infile
        os.makedirs(os.path.join(Configuration.TADs_dir,Configuration.file_to_process),exist_ok=True)
    
    logging.info(f"This script will run the file : {Configuration.file_to_process}")

    if args.step == None:
        # call trimming
        trimming.run_fastp(Configuration)

        # run hic-pro
        hic_pro.run_hic_pro(Configuration)

        # run juicebox
        hic_pro.run_juicebox(Configuration)

        # get matrixes and onTAD
        matrix_ontad.generate_mat_ontad(Configuration)
        
        # get compartments
        compartments.call_compartments(Configuration)

        # add cool
        convert_hic2cool.hic2cool(Configuration)

        # compress hi-c pro stuff
        cleanup.cleanup(Configuration)

        logging.info("pipeline completed")
        
    else:
        if "trimming" in args.step:
            trimming.run_fastp(Configuration)
        if "hicpro" in args.step:
            hic_pro.run_hic_pro(Configuration)
        if "juicebox" in args.step:
            hic_pro.run_juicebox(Configuration)
        if "onTAD" in args.step:
            matrix_ontad.generate_mat_ontad(Configuration)
        if "compartments" in args.step:
            compartments.call_compartments(Configuration)
        if "cool" in args.step:
            convert_hic2cool.hic2cool(Configuration)
        if "cleanup" in args.step:
            cleanup.cleanup(Configuration)


