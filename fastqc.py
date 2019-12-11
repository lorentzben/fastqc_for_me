# A python script that performs fastqc on samples and then outputs the results as human and machine readable
import subprocess
import os
import logging
from pathlib import Path
import argparse
from Bio import SeqIO
import numpy

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

    for score in average_qual_scores:
        if score[1] >= 20:
            logger.info(
                "All .fastq reads examined are over phread score of 20")
            pass
        else:
            logger.warning(
                "One or more of your reads have a average quality score of 20 or lower")
    return average_qual_scores
    logger.info("The ave qual score is: " + str(average_qual_scores))

def calculate_num_reads(files):
    num_table = []
    logger.info("calculating the number of reads") 
    for file in files:
        records = list(SeqIO.parse(file, "fastq"))
        num_table.append((file, len(records)))
    logger.info("table ocunting the number of reads :",str(num_table))
    return num_table

def calculate_len_reads():
    print("")
def create_machine_read_results():
    print("created machine readable results here: ")


def move_html_results():
    print("moved html copy of results here: ")


def check_quality_cutoffs():
    print("reads passed/failed cuttoffs")
    # TODO find what these standards should be for 16s


def main(args):
    set_up_logger(args.quiet)
    files = make_list_of_fastqs()
    quality = calculate_average_quality_score(files)
    print(calculate_num_reads(files))
    logger.info("Hi")

# pathlib package
# logging more intensly


if __name__ == "__main__":
    # Build Argument Parser in order to facilitate ease of use for user
    parser = argparse.ArgumentParser(description="Perform Automated Analysis and Formatting of Sequence Data")
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
