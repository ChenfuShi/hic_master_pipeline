#!/bin/bash --login
#$ -pe smp.pe 8
#$ -j y
#$ -o /mnt/iusers01/jw01/mdefscs4/psa_functional_genomics/master_HiC_analyzer/master_pipeline/logs

#$ -t 1-1

# CD to directory
cd /mnt/iusers01/jw01/mdefscs4/psa_functional_genomics/master_HiC_analyzer/master_pipeline


# activate all neeeded modules and packages
# source activate personal_software
source activate /mnt/iusers01/jw01/mdefscs4/communal_software/HiC-Pro/conda_hicpro3
# this contains fastp, ontad, bedtools
# other stuff for hicpro is automatically used

# module load apps/R/3.5.3/gcc-8.2.0+lapack-3.5.0+blas-3.6.0

module load tools/java/1.8.0
module load compilers/gcc/8.2.0

python hic_merger.py -i control1CD14_ARIMA -i control2CD14_ARIMA -i control3CD14_ARIMA -i control4CD14_ARIMA -i control5CD14_ARIMA -o control_CD14_ARIMA

# python hic_merger.py -i control1CD4_ARIMA -i control2CD4_ARIMA -i control3CD4_ARIMA -i control4CD4_ARIMA -i control5CD4_ARIMA -o control_CD4_ARIMA

# python hic_merger.py -i Patient1CD4_ARIMA -i Patient2CD4_ARIMA -i Patient3CD4_ARIMA -i Patient5CD4_ARIMA -i Patient6CD4_ARIMA -i Patient7CD4_ARIMA -i Patient8CD4_ARIMA -i Patient9CD4_ARIMA -i Patient10CD4_ARIMA -o PatientCD4_ARIMA

# python hic_merger.py -i Patient1CD14_ARIMA -i Patient2CD14_ARIMA -i Patient3CD14_ARIMA -i Patient5CD14_ARIMA -i Patient6CD14_ARIMA -i Patient7CD14_ARIMA -i Patient8CD14_ARIMA -i Patient9CD14_ARIMA -i Patient10CD14_ARIMA -o PatientCD14_ARIMA
