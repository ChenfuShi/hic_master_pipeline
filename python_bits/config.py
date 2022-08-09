########################################
# utility that contains a class that gets the configuration



########################################

import logging
import datetime

import json

class Config:
    """
    Class containing the parameters 
    """
    
    def __init__(self):
  
        self.RAW_input_dir = "/mnt/jw01-aruk-home01/projects/psa_functional_genomics/master_HiC_analyzer/reads_here"
        self.Trimmed_dir = "/mnt/iusers01/jw01/mdefscs4/scratch/master_HiC_analyzer/temp_trimming"
        self.Matrix_dir = "/mnt/iusers01/jw01/mdefscs4/scratch/master_HiC_analyzer/temp_matrix"
        self.HiC_pro_outs_dir = "/mnt/jw01-aruk-home01/projects/psa_functional_genomics/master_HiC_analyzer/hic-pro_outputs"
        self.HiC_pro_temp_dir = "/mnt/iusers01/jw01/mdefscs4/scratch/master_HiC_analyzer/hic-pro_outputs"
        self.Juicebox_dir = "/mnt/jw01-aruk-home01/projects/psa_functional_genomics/master_HiC_analyzer/juiceboxes"
        self.cool_dir = "/mnt/jw01-aruk-home01/projects/psa_functional_genomics/master_HiC_analyzer/cool"
        self.TADs_dir = "/mnt/jw01-aruk-home01/projects/psa_functional_genomics/master_HiC_analyzer/TADs"
        self.Reads_quality_dir = "/mnt/jw01-aruk-home01/projects/psa_functional_genomics/master_HiC_analyzer/fastp_reports"
        self.HiC_pro_loc = "/mnt/jw01-aruk-home01/projects/functional_genomics/bin/HiC-Pro/HiC-Pro_3.0.0_install/HiC-Pro_3.0.0/bin/HiC-Pro"
        self.hicpro2dense_loc = "/mnt/jw01-aruk-home01/projects/functional_genomics/bin/HiC-Pro/HiC-Pro_3.0.0_install/HiC-Pro_3.0.0/bin/utils/sparseToDense.py"
        self.hicpro2juicebox_loc = "/mnt/jw01-aruk-home01/projects/functional_genomics/bin/HiC-Pro/HiC-Pro_3.0.0_install/HiC-Pro_3.0.0/bin/utils/hicpro2juicebox.sh"
        self.juicer_tools_loc = "/mnt/jw01-aruk-home01/projects/functional_genomics/bin/juicer/juicer_tools_1.22.01.jar"
        self.compartments_loc = "/mnt/jw01-aruk-home01/projects/psa_functional_genomics/master_HiC_analyzer/compartments"
        self.gene_density_100kb = "/mnt/jw01-aruk-home01/projects/psa_functional_genomics/NEW_references/gene_density/hg38_100kb_gene_density_ucsc.bed"
        self.gene_density_250kb = "/mnt/jw01-aruk-home01/projects/psa_functional_genomics/NEW_references/gene_density/hg38_250kb_gene_density_ucsc.bed"
        self.OnTAD = "/mnt/jw01-aruk-home01/projects/functional_genomics/bin/OnTAD/OnTAD"
        self.merged_validpairs = "/mnt/iusers01/jw01/mdefscs4/scratch/master_HiC_analyzer/merged_validpairs"
        self.merged_sparsemat = "/mnt/iusers01/jw01/mdefscs4/scratch/master_HiC_analyzer/merged_sparsemat"
        self.logs_dir = "/mnt/jw01-aruk-home01/projects/psa_functional_genomics/master_HiC_analyzer/master_pipeline/logs"
        self.HiC_pro_HIND = "/mnt/jw01-aruk-home01/projects/functional_genomics/bin/HiC-Pro/HiC-Pro_3.0.0_install/HiC-Pro_3.0.0/HICPRO_config_HindIII_HiC.txt"
        self.HiC_pro_MBOI = "/mnt/jw01-aruk-home01/projects/functional_genomics/bin/HiC-Pro/HiC-Pro_3.0.0_install/HiC-Pro_3.0.0/HICPRO_config_MboI_HiChIP.txt"
        self.HiC_pro_ARIMA = "/mnt/jw01-aruk-home01/projects/functional_genomics/bin/HiC-Pro/HiC-Pro_3.0.0_install/HiC-Pro_3.0.0/HICPRO_config_Arima_HiC.txt"
        self.keep_hicpro_align = False
        
        self._init_logging()

        self.file_to_process = None
        
    def _init_logging(self):
        cur_date = datetime.datetime.now()
        
        logging.basicConfig(
            level=logging.INFO,
            format="%(levelname)s - %(message)s",
            handlers=[
                logging.StreamHandler()]) 
                # logging.FileHandler("{0}/{1}.log".format(self.logs_dir, f"{cur_date.year}-{cur_date.month}-{cur_date.day}_{cur_date.hour}.{cur_date.minute}.{cur_date.second}"), mode="a"),