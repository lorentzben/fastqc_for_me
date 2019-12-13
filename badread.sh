#!/usr/bin/env bash
sudo apt install python3.7-dev


git clone https://github.com/rrwick/Badread.git
pip3 install ./Badread

wget --output-document sratoolkit.tar.gz http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz
tar -vxzf sratoolkit.tar.gz
export PATH=$PATH:~/sratoolkit.2.9.6-1-ubuntu64/bin
fastq-dump SRX3407690

#TODO need to see how badread works with new genome, just make it messy 

git clone https://github.com/lh3/wgsim.git
cd wgsim 
gcc -g -O2 -Wall -o wgsim wgsim.c -lz -lm
export PATH=$PATH:~/sratoolkit.2.9.6-1-ubuntu64/bin
fastq-dump SAMN01911278

#these are bad qual good len and good qual good len 
wgsim -e 0 -d 500 -1 153 -2 153 SAMN01911278.fastq good.read1.fq good.read2.fq /dev/null
wgsim -e0.2 -d 500 -1 153 -2 153 SAMN01911278.fastq bad.read1.fq bad.read2.fq /dev/null