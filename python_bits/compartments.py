import os
import logging
import subprocess
from collections import defaultdict
import string
import random
from scipy import stats
import pandas as pd

def _get_eigens(Configuration, resolution, output_dir):
    hic_file = os.path.join(Configuration.Juicebox_dir, Configuration.file_to_process, Configuration.file_to_process + ".allValidPairs.hic")
    output_file = os.path.join(output_dir,Configuration.file_to_process + "_eigen_{chromosome}.txt")
    for chromosome in list(range(1,23)):
        proc = subprocess.run(["java", "-jar", Configuration.juicer_tools_loc, "eigenvector", "KR", 
        hic_file, str(chromosome), "BP", str(resolution * 1000), output_file.format(chromosome=chromosome), "-p"])
    return output_file

def _GET_compartments_corr(gene_density,file, resolution = 100000):
    def _flip_sign(current_eigen):
        merged = current_eigen.merge(pd.read_csv(gene_density,sep="\t",header=None), left_on=["chr","start","end"], right_on=[0,1,2],how="inner")
        merged = merged.fillna(0)
        corr = stats.pearsonr(merged["0_x"],merged[3])
        if corr[0] > 0:
            mul = 1
        else:
            mul = -1
        current_eigen[0] = current_eigen[0] * mul
        return current_eigen
    
    all_chr = pd.DataFrame()
    for i in list(range(1,23)):
        current_eigen = pd.read_csv(file.format(chromosome=i), header = None)
        current_eigen = current_eigen[:-2]
        current_eigen["id"] = list(range(len(current_eigen)))
        current_eigen["chr"] = "chr" + str(i)
        current_eigen["start"] = resolution * current_eigen["id"]
        current_eigen["end"] = resolution * (current_eigen["id"] +1)
        current_eigen = _flip_sign(current_eigen)
        all_chr = all_chr.append(current_eigen,sort=False)
        
    output = all_chr[["chr","start","end",0]].reset_index(drop=True)
    return output


def call_compartments(Configuration):
    for resolution in [100,250]:
        logging.info(f"Calling compartments for resolution {resolution}kb")
        output_dir = os.path.join(Configuration.compartments_loc,Configuration.file_to_process,str(resolution)+"kb")
        os.makedirs(output_dir,exist_ok = True)

        eignes = _get_eigens(Configuration, resolution, output_dir)
        if resolution == 100:
            compartments = _GET_compartments_corr(gene_density = Configuration.gene_density_100kb, file = eignes, resolution = resolution*1000)
        else:
            compartments = _GET_compartments_corr(gene_density = Configuration.gene_density_250kb, file = eignes, resolution = resolution*1000)
        compartments.to_csv(os.path.join(output_dir,Configuration.file_to_process + f"_compartments_corr_{resolution}kb.bdg"),sep="\t", header = False, index = False)


