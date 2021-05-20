# HiC analyser for University of Manchster servers

SGE batch system, SUBMIT_script for running and merger_script for merging different samples together

### How to use:

Generally there are a lot of parameters to set in the json config file. You can use CSF_chenfu_config.json as a baseline but you need to reconfigure the location of the scratch folders for your account.

#### Processing Hi-C data

1. Create symbolic links to the input data folder (reads_here). Each sample needs to be within one folder, will all the reads for all the lanes in there. The folder name needs to end in one of the following: ARIMA, HIND or MBOI. Set this based on the restriction enzyme that was used for your Hi-C library. It is very important that the name of the files are the same for the paired end execpt the R1.fastq.gz and R2.fastq.gz. So your files should look like SAMPLENAME_lane_R1.fastq.gz and SAMPLENAME_lane_R2.fastq.gz.

2. Set in SUBMIT_script.sh the number of samples you are going to process. To do so set #$ -t 1-N with N being the number of samples you have.

3. Submit the script to the CSF.


#### Merging of different samples for combined datasets

1. All the files need to be individually processed first.

2. After that modify the merger_script.sh and call the python script in the following way
    python hic_merger.py -i sample_1_ARIMA -i sample_2_ARIMA -i sample_N_ARIMA -o merged_ARIMA

3. Submit the script to the CSF


## Software versions

hic-pro: 3.0.0
fastp: 0.20.1
bedtools: 2.30.0
samtools: 1.9
bowtie2: 2.4.2
ontad: v1.2
java: 1.8.0
juicertools: 1.22.01