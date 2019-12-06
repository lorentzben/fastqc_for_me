#A python script that performs fastqc on samples and then outputs the results as human and machine readable
import subprocess
import os 

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

if __name__ == "main":
    parser = argparse.ArgumentParser(
        description="Perform Automatic Fastqc analysis and general parameter check")
    
    parser.add_argument('-c', action='store_true', default=False, required=False,
                        help="flag to use custom parameters, ignore for kelly lab parameters", dest='custom')
    parser.add_argument('-l', action='store', default=300, type=int, required=False,
                        help='determines the longest value permitted for sequences', dest='max_len')
    parser.add_argument('-p', action='store', default=2, type=int, required=False,
                        help='pre cluster value, higher is more stringent', dest='pre_clust')
    parser.add_argument('-s', action='store', type=int, required=False,
                        help='sub sample value, only applicable for custom runs', dest='sub_sample')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.0')

    args = parser.parse_args()
    #print(args)
    main(args)