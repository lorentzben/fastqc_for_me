#!/usr/bin/env bash

git clone https://github.com/rrwick/Badread.git
pip3 install ./Badread

wget --output-document sratoolkit.tar.gz http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz
tar -vxzf sratoolkit.tar.gz
export PATH=$PATH:~/sratoolkit.2.9.6-1-ubuntu64/bin
fastq-dump SRX3407690

#TODO need to see how badread works with new genome, just make it messy 