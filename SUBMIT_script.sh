#!/bin/bash --login
#$ -pe smp.pe 8 
#$ -j y
#$ -o /mnt/iusers01/jw01/mdefscs4/psa_functional_genomics/master_HiC_analyzer/master_pipeline/logs

#$ -t 1-1
INDEX=$((SGE_TASK_ID-1))
# CD to directory
cd /mnt/iusers01/jw01/mdefscs4/psa_functional_genomics/master_HiC_analyzer/master_pipeline


# activate all neeeded modules and packages
# source activate personal_software
source activate /mnt/jw01-aruk-home01/projects/functional_genomics/bin/HiC-Pro/conda_hicpro3
# this contains fastp, ontad, bedtools
# other stuff for hicpro is automatically used

# module load apps/R/3.5.3/gcc-8.2.0+lapack-3.5.0+blas-3.6.0

module load tools/java/1.8.0
module load compilers/gcc/8.2.0

# wait 20 seconds so that they don't crash into eachother
sleep $(($INDEX*20))
python ./master_hic_processor_allele.py
