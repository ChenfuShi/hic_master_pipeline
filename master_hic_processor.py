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
from python_bits import trimming, hic_pro, matrix_ontad, compartments


if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Wrapper function for all steps of Hi-C analysis')

    parser.add_argument("-i",'--input', dest='infile', action='store', required=False,
                        help='input folder to force. Will overwrite all ouputs')
    parser.add_argument("-c",'--config', dest='config', action='store', required=False,
                        help='Change configuration file')
    parser.add_argument("-s",'--step', dest='step', action='store', required=False,
                        help='chose step instead of running everything')

	# parse arguments
    args = parser.parse_args()

    # set up configuration object for all steps. this sets up logging as well
    if args.config:
        Configuration = Config(args.config)
    else:
        Configuration = Config()


    if args.infile == None:
        all_raws_present = os.listdir(Configuration.RAW_input_dir)

        # randomly wait a little bit of time to make sure we don't crash into eachother
        sleep(random()*20)
        all_processed = os.listdir(Configuration.TADs_dir)
        # chose the first one of the ones that are still not processed and run 
        if len(all_raws_present) == len(all_processed):
            logging.error("There were no new files to process")
            raise Exception

        for i in all_raws_present:
            if i not in all_processed:
                os.makedirs(os.path.join(Configuration.TADs_dir,i),exist_ok=True)
                Configuration.file_to_process = i
                break
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

        logging.info("pipeline completed")
        
    elif args.step == "compartments":
        compartments.call_compartments(Configuration)
