#!/bin/bash --login
#$ -pe smp.pe 8
#$ -j y
#$ -o /mnt/iusers01/jw01/mdefscs4/psa_functional_genomics/master_HiC_analyzer/master_pipeline/logs

#$ -t 1-1

# CD to directory
cd /mnt/iusers01/jw01/mdefscs4/psa_functional_genomics/master_HiC_analyzer/master_pipeline


# activate all neeeded modules and packages
source activate personal_software
# this contains fastp, ontad, bedtools
# other stuff for hicpro is automatically used

module load apps/R/3.5.3/gcc-8.2.0+lapack-3.5.0+blas-3.6.0

module load tools/java/1.8.0
module load compilers/gcc/8.2.0


python hic_merger.py -i test_ARIMA -i CD4_arima_sample1_from_jenny_ARIMA -i CD4_arima_sample2_from_jenny_ARIMA -o test_merging_CD4_ARIMA