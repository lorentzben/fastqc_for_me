#A python script that performs fastqc on samples and then outputs the results as human and machine readable
import subprocess
import os 
import logging

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

def call_fastqc():
    print("fastqc run finished")

def create_machine_read_results():
    print("created machine readable results here: ")

def move_html_results():
    print("moved html copy of results here: ")

def check_quality_cutoffs():
    print("reads passed/failed cuttoffs")
    #TODO find what these standards should be for 16s 

def main(args):
    if(args.custom):
        print("do something")
    else:
        print("do the other thing")

#pathlib package 
# logging more intensly

if __name__ == "__main__":
    # Build Argument Parser in order to facilitate ease of use for user
    parser=argparse.ArgumentParser(
        description = "Perform Automated Analysis and Formatting of Sequence Data")
    parser.add_argument('-n', action = 'store', required = True,
                        help = "name for analysis, will be filename for resultant files", dest = 'job_name')
    parser.add_argument('-c', action = 'store_true', default = False, required = False,
                        help = "flag to use custom parameters, ignore for kelly lab parameters", dest = 'custom')
    parser.add_argument('-l', action = 'store', default = 300, type = int, required = False,
                        help = 'determines the longest value permitted for sequences', dest = 'max_len')
    parser.add_argument('-p', action = 'store', default = 2, type = int, required = False,
                        help = 'pre cluster value, higher is more stringent', dest = 'pre_clust')
    parser.add_argument('-s', action = 'store', type = int, required = False,
                        help = 'sub sample value, only applicable for custom runs', dest = 'sub_sample')
    parser.add_argument('-q', '--quiet', action = 'store_true', default = False,
                        help = "Reduces the amount of text printed to terminal, check logfiles more often", dest = 'quiet')
    parser.add_argument('-v', '--version', action = 'version',
                        version = '%(prog)s 1.0')

    args=parser.parse_args()
    
    #wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.8.zip