#!/bin/bash --login
#$ -pe smp.pe 8
#$ -j y
#$ -o /mnt/iusers01/jw01/mdefscs4/psa_functional_genomics/master_HiC_analyzer/master_pipeline/logs

#$ -t 1-45
INDEX=$((SGE_TASK_ID-1))
# CD to directory
cd /mnt/iusers01/jw01/mdefscs4/psa_functional_genomics/master_HiC_analyzer/hic-pro_outputs


FILES=(CD4_arima_sample1_from_jenny_ARIMA
CD4_arima_sample2_from_jenny_ARIMA
control1CD14_ARIMA
control1CD4_ARIMA
control2CD14_ARIMA
control2CD4_ARIMA
control3CD14_ARIMA
control3CD4_ARIMA
control4CD14_ARIMA
control4CD4_ARIMA
control5CD14_ARIMA
control5CD4_ARIMA
HiC_RA_A1_HIND
HiC_RA_A2_HIND
HiC_RA_A3_HIND
HiC_RA_R_1_HIND
HiC_RA_R_2_HIND
HiC_RA_R3_HIND
jia_BTH269_MBOI
jia_BTH316_MBOI
jia_BTH351_MBOI
Newman_1_HiC_ARIMA
Newman_2_HiC_ARIMA
Newman_3_HiC_ARIMA
Newman_4_HiC_ARIMA
Patient10CD14_ARIMA
Patient10CD4_ARIMA
Patient1CD14_ARIMA
Patient1CD4_ARIMA
Patient2CD14_ARIMA
Patient2CD4_ARIMA
Patient3CD14_ARIMA
Patient3CD4_ARIMA
Patient4CD14_ARIMA
Patient4CD4_ARIMA
Patient5CD14_ARIMA
Patient5CD4_ARIMA
Patient6CD14_ARIMA
Patient6CD4_ARIMA
Patient7CD14_ARIMA
Patient7CD4_ARIMA
Patient8CD14_ARIMA
Patient8CD4_ARIMA
Patient9CD14_ARIMA
Patient9CD4_ARIMA)

cd ${FILES[$INDEX]}
cd hic_results
cd data
find -L ./ -maxdepth 6 -type f ! -name '*.gz' -print0 | xargs -L1 -P8 -0 gzip
cd ..
cd matrix
find -L ./ -maxdepth 6 -type f ! -name '*.gz' -print0 | xargs -L1 -P8 -0 gzip