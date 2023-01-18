#!/bin/bash --login
#$ -pe smp.pe 8
#$ -j y
#$ -o /mnt/iusers01/jw01/mdefscs4/psa_functional_genomics/master_HiC_analyzer/master_pipeline/logs
#$ -l mem256
#$ -t 1-1

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

# python hic_merger.py -i control1CD14_ARIMA -i control2CD14_ARIMA -i control3CD14_ARIMA -i control4CD14_ARIMA -i control5CD14_ARIMA -i Patient1CD14_ARIMA -i Patient2CD14_ARIMA -i Patient3CD14_ARIMA -i Patient5CD14_ARIMA -i Patient6CD14_ARIMA -i Patient7CD14_ARIMA -i Patient8CD14_ARIMA -i Patient9CD14_ARIMA -i Patient10CD14_ARIMA -o ALL_CD14_ARIMA

# python hic_merger.py -i control1CD4_ARIMA -i control2CD4_ARIMA -i control3CD4_ARIMA -i control4CD4_ARIMA -i control5CD4_ARIMA -i Patient1CD4_ARIMA -i Patient2CD4_ARIMA -i Patient3CD4_ARIMA -i Patient5CD4_ARIMA -i Patient6CD4_ARIMA -i Patient7CD4_ARIMA -i Patient8CD4_ARIMA -i Patient9CD4_ARIMA -i Patient10CD4_ARIMA -o ALL_CD4_ARIMA

# python hic_merger.py -i control1CD14_ARIMA -i control2CD14_ARIMA -i control3CD14_ARIMA -i control4CD14_ARIMA -i control5CD14_ARIMA -o control_CD14_ARIMA

# python hic_merger.py -i control1CD4_ARIMA -i control2CD4_ARIMA -i control3CD4_ARIMA -i control4CD4_ARIMA -i control5CD4_ARIMA -o control_CD4_ARIMA

# python hic_merger.py -i Patient1CD4_ARIMA -i Patient2CD4_ARIMA -i Patient3CD4_ARIMA -i Patient5CD4_ARIMA -i Patient6CD4_ARIMA -i Patient7CD4_ARIMA -i Patient8CD4_ARIMA -i Patient9CD4_ARIMA -i Patient10CD4_ARIMA -o PatientCD4_ARIMA

# python hic_merger.py -i Patient1CD14_ARIMA -i Patient2CD14_ARIMA -i Patient3CD14_ARIMA -i Patient5CD14_ARIMA -i Patient6CD14_ARIMA -i Patient7CD14_ARIMA -i Patient8CD14_ARIMA -i Patient9CD14_ARIMA -i Patient10CD14_ARIMA -o PatientCD14_ARIMA

# python hic_merger.py -o all_cd8_test -i PSA4920_CD8_ARIMA -i PSA4941_CD8_ARIMA -i PSA4942_CD8_ARIMA -i PSA4943_CD8_ARIMA -i PSA4954_CD8_ARIMA -i PSA4960_CD8_ARIMA -i PSA4961_CD8_ARIMA -i PSA4962_CD8_ARIMA -i PSA4963_CD8_ARIMA -i PsA4950_CD8_ARIMA -i NRHV121_CD8_ARIMA -i NRHV321_CD8_ARIMA -i NRHV171CD8_ARIMA -i PsA4958CD8_ARIMA -i PsA5009CD8_ARIMA -i PsA5024CD8_ARIMA -i PsA5037CD8_ARIMA -i PsA5018CD8_ARIMA -i PsA5019CD8_ARIMA -i NRHV324CD8_ARIMA -i PsA5022CD8_ARIMA -i PsA5017CD8_ARIMA -i PsA5021CD8_ARIMA -i PsA5020CD8_ARIMA -i PsA5023CD8_ARIMA -i PsA5026CD8_ARIMA

# python hic_merger.py -o all_cartilage -i H_Cart_ARIMA -i P663H_Cart_ARIMA -i P674H_Cart_ARIMA

# python hic_merger.py -o all_jurkat -i JurkatE6_1_ARIMA -i Jurkat_all_old_ARIMA

python hic_merger.py -o all_cartilage_oct_2022 -i H_Cart_ARIMA -i P663H_Cart_ARIMA -i P674H_Cart_ARIMA -i P698_ARIMA -i P702_ARIMA -i P710_ARIMA -i P713_ARIMA -i P714_ARIMA -i P718_ARIMA