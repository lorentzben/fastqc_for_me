# A python script that performs fastqc on samples and then outputs the results as human and machine readable
import subprocess
import os
import logging
from pathlib import Path
import argparse
from Bio import SeqIO
import numpy
import operator
import json
import codecs
import re
from itertools import takewhile

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Logging handler which catches EVERYTHING
file_logger = logging.FileHandler('fast_parser.log')
file_logger.setLevel(logging.DEBUG)
# Logging handler which logs less
console_logger = logging.StreamHandler()


def set_up_logger(quiet):
    if quiet:
        console_logger.setLevel(logging.WARNING)
    else:
        console_logger.setLevel(logging.INFO)


# Formats the logs so they are pretty
logFormatter = '%(asctime)s- %(name)s - %(lineno)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(logFormatter)
file_logger.setFormatter(formatter)
console_logger.setFormatter(formatter)

# adds handlers to logger
logger.addHandler(file_logger)
logger.addHandler(console_logger)


def create_file_struct():
    q = Path.cwd()
    results_to_process = []
    for item in q.iterdir():
        if item.is_dir():
            logger.debug("dir found: %s" % item)
            results_to_process.append(item)
    return results_to_process
 

def create_result_table(results_to_process):
    z = Path.cwd()
    result_table = []
    for directory in results_to_process:
        os.chdir(directory)
        result = parse_fastq()
        #result = tuple([tuple([Kelly001,116603]),tuple([301, 36])])
        seq_name = result[0][0].strip()
        tot_seq = result[0][1]
        seq_len = result[1][0]
        mean_qual = result[1][1]
        logger.debug([seq_name,tot_seq,seq_len,mean_qual])
        result_table.append([seq_name,tot_seq,seq_len,mean_qual])
    return result_table

def parse_fastq():
    temp_name = ''
    temp_seq = ''
    temp_len = ''
    temp_qual = ''
    parse = False
    base_table = []
    with open('fastqc_data.txt') as f:
        for line in f:
            if line.startswith('>>END_MODULE'):
                parse = False
            elif line.startswith('>>Per base sequence quality'):
                parse= True
            elif parse:
                base_table.append(str(line))
            else:  
                continue
    with open('fastqc_data.txt') as p:
        data = p.readlines()
    for line in data:
        if re.match("(.*)Filename(.*)",line):
            temp_name = line
        elif re.match("(.*)Total Sequences(.*)",line):
            temp_seq = line
        elif re.match("(.*)Sequence length(.*)",line):
            temp_len = line

    logger.debug(temp_name)
    logger.debug(temp_seq)
    logger.debug(temp_len)

    #editing the base table to remove heading and then format in a manner to calc mean
    base = numpy.delete(base_table,0,0)
    quals = numpy.loadtxt(base, delimiter='\t',usecols=[1])
    fin_qual = numpy.mean(quals)

    name = temp_name.split('\t')
    seq = temp_seq.split('\t')
    length = temp_len.split('\t')

    logger.debug(name)
    logger.debug(seq)
    logger.debug(length)

    fin_name = name[1].strip()
    fin_seq = float(seq[1].strip())
    fin_len = int(length[1].strip())

    logger.debug(fin_name)
    logger.debug(fin_seq)
    logger.debug(fin_len)

    logger.debug("processed file")

    result = tuple([tuple([fin_name,fin_seq]),tuple([fin_len,fin_qual])])
    return result


def main(args):
    set_up_logger(args.quiet)
    p = Path.cwd()
    #TODO find out where we are
    files = create_file_struct()
    table = create_result_table(files)
    logger.info(table)
    with open ("output.txt",'w') as filehandle:
        for line in table:
            filehandle.write(str(line))
    #print(table)


if __name__ == "__main__":
    # Build Argument Parser in order to facilitate ease of use for user
    parser = argparse.ArgumentParser(
        description="Perform Automated Analysis and Formatting of Sequence Data")
    parser.add_argument('-n', action='store', required=True,
                        help="name for fastqc output dir", dest='dir_name')
    parser.add_argument('-q', '--quiet', action='store_true', default=False,
                        help="Reduces the amount of text printed to terminal, check logfiles more often", dest='quiet')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.0')

    args = parser.parse_args()
    main(args)
