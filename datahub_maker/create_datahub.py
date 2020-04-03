import pandas as pd
import os
import subprocess

sample_info = pd.read_excel("/mnt/iusers01/jw01/mdefscs4/psa_functional_genomics/master_HiC_analyzer/master_pipeline/datahub_maker/hichip_data.xlsx")


datahub=pd.DataFrame()
for index,row in sample_info.iterrows():
    datahub = datahub.append({"type":"longrange","name":row["proper_name"]+"_hichipper_default",
    "url":"http://bartzabel.ls.manchester.ac.uk/worthingtonlab/psa_functional_genomics/uniform_data/hichipper_default/"+row["proper_name"]+".washu.FDR0.10.bed.gz",
     "options":{"displayMode": "arc"},"metadata" : {"sample" : row["proper_name"]}},
     ignore_index = True)
    datahub = datahub.append({"type":"bed","name":row["proper_name"]+"_hichipper_anchors",
    "url":"http://bartzabel.ls.manchester.ac.uk/worthingtonlab/psa_functional_genomics/uniform_data/hichipper_default/"+row["proper_name"]+".anchors.bed.gz",
    "metadata" : {"sample" : row["proper_name"]}},
     ignore_index = True)
    datahub = datahub.append({"type":"longrange","name":row["proper_name"]+"_hichipper_mypeaks",
    "url":"http://bartzabel.ls.manchester.ac.uk/worthingtonlab/psa_functional_genomics/uniform_data/hichipper_mypeaks/"+row["proper_name"]+".washu.FDR0.10.bed.gz", 
    "options":{"displayMode": "arc"},"metadata" : {"sample" : row["proper_name"]}},
     ignore_index = True)
    datahub = datahub.append({"type":"bed","name":row["proper_name"]+"_mysoft_peaks",
    "url":"http://bartzabel.ls.manchester.ac.uk/worthingtonlab/psa_functional_genomics/uniform_data/chip_peaks_and_graphs/"+row["proper_name"]+"_peaks.bed.gz",
    "metadata" : {"sample" : row["proper_name"]}},
     ignore_index = True)
    datahub = datahub.append({"type":"bedGraph","name":row["proper_name"]+"_mysoft_bedgraph",
    "url":"http://bartzabel.ls.manchester.ac.uk/worthingtonlab/psa_functional_genomics/uniform_data/chip_peaks_and_graphs/"+row["proper_name"]+"_bedgraph.bdg.gz",
    "metadata" : {"sample" : row["proper_name"]}},
     ignore_index = True)
    datahub = datahub.append({"type":"longrange","name":row["proper_name"]+"_stringent_fithichip",
    "url":"http://bartzabel.ls.manchester.ac.uk/worthingtonlab/psa_functional_genomics/uniform_data/fithichip/"+row["proper_name"]+"_stringent_Q0.01_WashU.bed.gz", 
    "options":{"displayMode": "arc"},"metadata" : {"sample" : row["proper_name"]}},
     ignore_index = True) 
    datahub = datahub.append({"type":"longrange","name":row["proper_name"]+"_stringent_merged_fithichip",
    "url":"http://bartzabel.ls.manchester.ac.uk/worthingtonlab/psa_functional_genomics/uniform_data/fithichip/"+row["proper_name"]+"_stringent_merged_Q0.01_WashU.bed.gz", 
    "options":{"displayMode": "arc"},"metadata" : {"sample" : row["proper_name"]}},
     ignore_index = True) 

extra_info = pd.read_excel("/mnt/iusers01/jw01/mdefscs4/psa_functional_genomics/master_HiC_analyzer/master_pipeline/datahub_maker/extra_data.xlsx")
for index,row in extra_info.iterrows():
     datahub = datahub.append({"type":row["type"],"name":row["name"],
    "url":row["url"],
     "metadata" : {"sample" : row["sample"]}},
     ignore_index = True)

print(datahub)
datahub.to_json("psa_fungen_datahub.json",orient="records")