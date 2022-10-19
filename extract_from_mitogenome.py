#!/usr/bin/env python3

import argparse

p = argparse.ArgumentParser()

# Arguments to accept files from the command line. -f [fasta file] -r [bp range]
# Use example: ./extract_fasta.py -f file.fasta -r 1..600

p.add_argument("-f", type=str, required=True, help="Input file in fasta format")
p.add_argument("-r", type=str, required=True,help="integer number of the range of the seq to be extracted, GenBank format. e.g., 1..600")

args = p.parse_args()
Fasta_file = args.f
seq_range = args.r
fh = open(Fasta_file, 'r')
start = int(seq_range.split("..")[0])-1
end = int(seq_range.split("..")[1])

header = []
seq = []

for line in fh:
    line = line.strip("\n")
    if ">" == line[0]:
        print(line)
    else:
        print(line[start:end])
        
fh.close()
    