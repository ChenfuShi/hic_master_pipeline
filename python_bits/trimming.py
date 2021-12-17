########################################
# script for running fastp



########################################

import os
import logging
import subprocess


def run_fastp(Configuration):
    """Files need to be structured this way:
    - everything needs to be the same except R1 and R2
    - each couple of different names is going to be processed as a pair with a parallel call to fastp"""

    RAW_files = os.listdir(os.path.join(Configuration.RAW_input_dir,Configuration.file_to_process))
    RAW_files = [f for f in RAW_files if f.endswith(".gz")]
    if len(RAW_files) % 2 != 0:
        logging.error("There wasn't an even number of files in the RAW directory")
        raise Exception

    lanes, form = _get_bases(RAW_files)
    logging.info(f"Identified {len(lanes)} lanes to process")
    logging.info(f"Running fastp")
    if len(lanes) <= 4:
        _run_fastp_batch(lanes, form, Configuration)
    else:
        if len(lanes) <= 8:
            _run_fastp_batch(lanes[0:4], form, Configuration)
            _run_fastp_batch(lanes[4:], form, Configuration)
        else:
            _run_fastp_batch(lanes[0:4], form, Configuration)
            _run_fastp_batch(lanes[4:8], form, Configuration)
            _run_fastp_batch(lanes[8:], form, Configuration) # if this happens ahah

    logging.info(f"Finished running fastp")


def _run_fastp_batch(lanes, form, Configuration):
    processes = []
    input_dir = os.path.join(Configuration.RAW_input_dir,Configuration.file_to_process)
    output_dir = os.path.join(Configuration.Trimmed_dir,Configuration.file_to_process,Configuration.file_to_process)
    quality_dir = os.path.join(Configuration.Reads_quality_dir,Configuration.file_to_process)
    os.makedirs(output_dir,exist_ok=True)
    os.makedirs(quality_dir,exist_ok=True)
    for lane in lanes:
        if form == "fastq.gz":
            proc = subprocess.Popen(["fastp","-i",os.path.join(input_dir,lane)+"R1.fastq.gz","-I",os.path.join(input_dir,lane)+"R2.fastq.gz",
                "-o",os.path.join(output_dir,lane)+"R1.fastq.gz","-O",os.path.join(output_dir,lane)+"R2.fastq.gz",
                "-r","-h",os.path.join(quality_dir,lane)+"_fastp.html","-j",os.path.join(quality_dir,lane)+"_fastp.json",
                "-R",lane,"-p"])
        elif form == "fq.gz":
            proc = subprocess.Popen(["fastp","-i",os.path.join(input_dir,lane)+"1.fq.gz","-I",os.path.join(input_dir,lane)+"2.fq.gz",
                "-o",os.path.join(output_dir,lane)+"R1.fastq.gz","-O",os.path.join(output_dir,lane)+"R2.fastq.gz",
                "-r","-h",os.path.join(quality_dir,lane)+"_fastp.html","-j",os.path.join(quality_dir,lane)+"_fastp.json",
                "-R",lane,"-p"])
        processes.append(proc)
    for p in processes:
        p.wait()


def _get_bases(files):
    """function used to extract the lanes from the files"""
    def __rchop(thestring, ending):
        if thestring.endswith(ending):
            return thestring[:-len(ending)]
        return thestring

    files_present = set()
    for l in files:
        if l.endswith("fastq.gz"):
            files_present.add(__rchop(__rchop(l,"R1.fastq.gz"),"R2.fastq.gz"))
            form = "fastq.gz"
        elif l.endswith("fq.gz"):
            files_present.add(__rchop(__rchop(l,"1.fq.gz"),"2.fq.gz"))
            form = "fq.gz"

    if len(files_present)*2 != len(files):
        logging.error("Couldn't identify the base name, please check raw files naming")
        raise Exception
    return list(files_present), form