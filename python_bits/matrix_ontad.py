########################################
# script for running matrix generation and ontad



########################################

import os
import logging
import subprocess
from collections import defaultdict
import string
import random



def generate_mat_ontad(Configuration):

    # this is a fucking hack, not needed anymore because he updated to python 3
    # python2_loc = "/mnt/iusers01/jw01/mdefscs4/psa_functional_genomics/HiChIP_test/software/HiChIP_test2/bin/python"

    chromosomes=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","X"]
    chr_size=["248956422","242193529","198295559","190214555","181538259","170805979","159345973","145138636","138394717","133797422","135086622","133275309","114364328","107043718","101991189","90338345","83257441","80373285","58617616","64444167","46709983","50818468","156040895"]


    for resolution in ["20000","40000"]:
        logging.info(f"Creating dense matrixes for {resolution} resolution")
        abs_bed = os.path.join(Configuration.HiC_pro_outs_dir,Configuration.file_to_process,"hic_results","matrix",
            Configuration.file_to_process,"raw",resolution,Configuration.file_to_process + "_" +resolution + "_abs.bed")
        matrixes = os.path.join(Configuration.HiC_pro_outs_dir,Configuration.file_to_process,"hic_results","matrix",
            Configuration.file_to_process,"iced",resolution,Configuration.file_to_process + "_" +resolution + "_iced.matrix")
        mat_outdir = os.path.join(Configuration.Matrix_dir,Configuration.file_to_process,resolution)
        os.makedirs(mat_outdir,exist_ok=True)
        subprocess.run(["python",Configuration.hicpro2dense_loc,"-b",abs_bed,matrixes,"--perchr"],cwd=mat_outdir)


        logging.info(f"Running OnTad for {resolution} resolution")
        ontad_output = os.path.join(Configuration.TADs_dir,Configuration.file_to_process,resolution)
        os.makedirs(ontad_output,exist_ok=True)
        for cur_chro in range(len(chromosomes)):
            dense_mat = os.path.join(mat_outdir,Configuration.file_to_process +"_" +resolution + "_iced_chr" + chromosomes[cur_chro] + "_dense.matrix")
            cur_out = os.path.join(ontad_output,"OnTAD" + Configuration.file_to_process + "chr" + chromosomes[cur_chro])
            throwaway_file = os.path.join(mat_outdir, "OnTAD_output")
            with open(os.path.join(ontad_output,"OnTAD_all_chr.bed"), "w") as ontad_throwaway:
                subprocess.run([Configuration.OnTAD,dense_mat,"-o",cur_out,"-maxsz","100","-bedout",chromosomes[cur_chro],chr_size[cur_chro],resolution], stdout = ontad_throwaway)

        with open(os.path.join(ontad_output,"OnTAD_all_chr.bed"), "w") as combined_output:
            subprocess.run("cat OnTAD*.bed",shell=True,stdout=combined_output,cwd = ontad_output)
        with open(os.path.join(ontad_output,"OnTAD_all_chr_sorted.bed"), "w") as combined_output:    
            subprocess.run(["bedtools", "sort", "-i", os.path.join(ontad_output,"OnTAD_all_chr.bed")],stdout=combined_output,cwd = ontad_output)           
        subprocess.run(["bgzip", os.path.join(ontad_output,"OnTAD_all_chr_sorted.bed"),"-f"],cwd = ontad_output)
        subprocess.run(["tabix", "-p", "bed", os.path.join(ontad_output,"OnTAD_all_chr_sorted.bed.gz"),"-f"],cwd = ontad_output)

        logging.info("OnTAD for current resolution done")