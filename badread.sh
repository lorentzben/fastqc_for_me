#!/usr/bin/env bash

wget --output-document sratoolkit.tar.gz http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz
tar -vxzf sratoolkit.tar.gz
export PATH=$PATH:~/sratoolkit.2.9.6-1-ubuntu64/bin
fastq-dump SAMN01911278

git clone https://github.com/lh3/wgsim.git
cd wgsim 
gcc -g -O2 -Wall -o wgsim wgsim.c -lz -lm

#Good quality good length
wgsim -e 0 -d 500 -1 153 -2 153 SAMN01911278.fastq good_q_good_l.read1.fq good_q_good_l.read2.fq /dev/null
#gives a perfect phred score for reads
sed -i 's/I/h/g' good_q_good_l.read1.fq
sed -i 's/I/h/g' good_q_good_l.read2.fq
#Bad quality good length
wgsim -e0.2 -d 500 -1 153 -2 153 SAMN01911278.fastq bad_q_good_l.read1.fq bad_q_good_l.read2.fq /dev/null
#Good quality short len
wgsim -e0 -d 500 -1 100 -2 100 SAMN01911278.fastq good_q_short_l.read1.fq good_q_short_l.read2.fq /dev/null
sed -i 's/I/h/g' good_q_short_l.read1.fq
sed -i 's/I/h/g' good_q_short_l.read2.fq
#Good quality long len
wgsim -e0 -d 500 -1 300 -2 300 SAMN01911278.fastq good_q_long_l.read1.fq good_q_long_l.read2.fq /dev/null
sed -i 's/I/h/g' good_q_long_l.read1.fq
sed -i 's/I/h/g' good_q_long_l.read2.fq
#Bad quality short len
wgsim -e0.2 -d 500 -1 100 -2 100 SAMN01911278.fastq bad_q_short_l.read1.fq bad_q_short_l.read2.fq /dev/null
#Bad quality long len
wgsim -e0.2 -d 500 -1 300 -2 300 SAMN01911278.fastq bad_q_long_l.read1.fq bad_q_long_l.read2.fq /dev/null