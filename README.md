FastQC For Me
-------------------------------------------------
Quality control is an integral step in 16s analysis. It is important to ensure that quality data is being analysed. Tools such as fastQC do make quality control easier, however there is not a native way to have a human and machine readable result for a project's worth of samples. This script aims to produce a human-readable table of statistics from a folder of fastqc data. 
## Prerequisities
* Linux
* Python 3 (installed and in path)
* pip3 v.19.2.1
* FastQC v.0.11.8 (installed and in path)

## Install

```shell
$ git clone git@github.com:lorentzben/fastqc_for_me.git
```
After cloning a folder called fastqc_for_me will be created. Inside will be this README and fast_parser.py

## Help
```shell
$ python3 fast_parser.py -h
usage: fast_parser.py [-h] -n DIR_NAME [-c] [-q] [-v]

Perform Automated Analysis and Formatting of Sequence Data

optional arguments:
  -h, --help     show this help message and exit
  -n DIR_NAME    name for fastqc output dir
  -c             writes the parsed information to console in a way that is
                 easier to read than the log file format
  -q, --quiet    Reduces the amount of text printed to terminal, check
                 logfiles more often
  -v, --version  show program's version number and exit

```


## Running 
```shell
$chmod +x fast_parser.py
$ ./fastqc PROJECTNAME* --outdir=PROJECTNAME_data --extract
$ cd PROJECTNAME_data
$ python3 fast_parser.py -n NAME -c
```
Ensure that the unpack illumina 

## Output
```shell
Kelly003-NPS3_S87_L001_R1_001.fastq 107119.0 301 34.36016259816598
Kelly005-NPS5_S89_L001_R1_001.fastq 122292.0 301 34.28974008207934
```
example output where the columns are:
FILENAME SEQUENCE_COUNT SEQUENCE_LEN AVERAGE_QUAL_SCORE

this table is also written in the fastq_output.csv

## Current Files
* fastqc.py
* README.md

## Version
* Version 1.0

## Author
* Ben Lorentz

