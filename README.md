FastQC For Me
-------------------------------------------------
Quality control is an integral step in 16s analysis. It is important to ensure that quality data is being analysed. Tools such as fastQC do make quality control easier, however there is not a native way to have a human and machine readable result for a project's worth of samples. This script aims to produce a folder of human readable html documents, as well as a machine readable table of stats based on the fastqc run on a folder of fastq files, to aid in downstream analysis.
## Prerequisities
* Linux
* Python 3 (installed and in path)
* pip3 v.19.2.1
* FastQC v.0.11.8 (installed and in path)

## Install

```shell
$ git clone git@github.com:lorentzben/fastqc_for_me.git
```
TODO fill out what else will be in here
After cloning a folder called fastqc_for_me will be created. Inside will be this README and fastqc.py

## Help
```shell
$ python3 fastqc.py -h 

```


## Running 
```shell
$ chmod +x unpack_illumina.py
$ python3 unpack_illumina.py -n NAME
```
Ensure that the name of the nested folder from basespace The results of analysis will be placed ____ 

TODO fill in where this location is


## Output
TODO fill in names

Inside of the directory ______there will be _______

## Current Files
* fastqc.py
* README.md

## Version
* Version 1.0

## Author
* Ben Lorentz

## Future Plans
* Call fastqc on all .fastq files in directory
* Move resultant html files into one output dir
* Parse txt files for average read len and average quality score
* Determine cutoffs for qual score and read len
* Create tsv file and python object (json dump) of machine readble reults
* Implememt unit testing using the unittest package
* Implememnt logging at info and debugging levels
* Move final files into a output directory 
