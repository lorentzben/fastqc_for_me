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

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Logging handler which catches EVERYTHING
file_logger = logging.FileHandler('fastq_for_me.log')
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

# creates a list with path to fastq files in current dir


def make_list_of_fastqs():
    current_dir = Path('.')
    fastqs = list(current_dir.glob('*.fastq'))
    logger.info("The fastq files found are: " + str(fastqs))
    return fastqs


def calculate_average_quality_score(files):

    # will hold tuples of seq name and average qual score
    average_qual_scores = []
    # creates a list of quality scores and appends it to a list

    logger.info("Calculating average quality score of reads and adding to list")
    for read in files:
        for record in SeqIO.parse(read, "fastq"):

            quals = record.letter_annotations["phred_quality"]
        average_qual_scores.append(
            (read, numpy.around(numpy.mean(quals), decimals=0)))
    # checks to see if qual score is less than 20
    for score in average_qual_scores:
        if score[1] >= 20:
            logger.info(
                "All .fastq reads examined are over phread score of 20")
            pass
        else:
            logger.warning(
                "One or more of your reads have a average quality score of 20 or lower")
    for item in average_qual_scores:
        logger.debug(item[1])

    logger.info("The ave qual score is: " + str(average_qual_scores))
    return average_qual_scores


# calculates the number of reads
def calculate_num_reads(files):
    num_table = []
    logger.info("calculating the number of reads")
    for file in files:
        records = list(SeqIO.parse(file, "fastq"))
        num_table.append((file, len(records)))
    logger.info("table counting the number of reads :" + str(num_table))
    return num_table

# calculates the length of reads as well as mean and median


def calculate_len_reads(files):
    len_table = []
    logger.info("calculating the length of reads")
    for file in files:
        length = [len(record) for record in SeqIO.parse(file, "fastq")]
        len_table.append((file, (numpy.mean(length), numpy.median(length))))
    logger.info(
        "table with read, mean, median of len of reads: " + str(len_table))
    return len_table

# forms pythoon object writes out to file


def create_machine_read_results(files, quality, num_reads, len_reads, comp):
    print("sorting based on filename")
    files.sort()
    quality.sort()
    num_reads.sort()
    len_reads.sort()
    tab_list = []
    for i in range(0, len(files)):
        filename = quality[i][0].name
        qual_score = quality[i][1]
        count_read = num_reads[i][1]
        mean_read = len_reads[i][1][0]
        med_read = len_reads[i][1][1]
        tab_list.append(
            [filename, qual_score, count_read, mean_read, med_read])

    headers = ['name', 'ave qual score',
               'read count', 'ave read len', 'med read len']
    table = numpy.array(headers)
    table_with_headings = numpy.append(table, numpy.array(tab_list))
    logging.info(numpy.array2string(table_with_headings).replace(
        '[[', '[').replace(']]', ']'))
    if not comp:
       # writes python object into serialized json file
        listed_table = table.tolist()
        json.dump(listed_table, codecs.open('table.json', 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)


def create_human_read_results():
    # parses a python object from json
    table_text = codecs.open('table.json', 'r', encoding='utf-8').read()
    table_list = json.loads(table_text)
    table = np.array(table_list)

    print(numpy.array2string(table).replace('[[', '[').replace(']]', ']'))


def check_quality_cutoffs():
    print("reads passed/failed cuttoffs")
    # TODO find what these standards should be for 16s


def main(args):
    set_up_logger(args.quiet)
    files = make_list_of_fastqs()
    quality = calculate_average_quality_score(files)
    num_reads = calculate_num_reads(files)
    len_reads = calculate_len_reads(files)
    create_machine_read_results(
        files, quality, num_reads, len_reads, args.comp)


# pathlib package
# logging more intensly


if __name__ == "__main__":
    # Build Argument Parser in order to facilitate ease of use for user
    parser = argparse.ArgumentParser(
        description="Perform Automated Analysis and Formatting of Sequence Data")
    parser.add_argument('-r', '--readable', action='store_true', default=True,
                        help='creates a human readable output of the quality assesment', dest='human')
    parser.add_argument('-f', '--no-file', action='store_true', default=False,
                        help='does not create a computer readable file must use -r flag for human readability', dest='comp')
    parser.add_argument('-q', '--quiet', action='store_true', default=False,
                        help="Reduces the amount of text printed to terminal, check logfiles more often", dest='quiet')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.0')

    args = parser.parse_args()
    main(args)

    # wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.8.zip
