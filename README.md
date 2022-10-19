# Rhoadsia_clade_scripts
Script to extract sequences from mitogenomes (fasta dowloaded from NCBI) by specifying nucleotide position as reported in NCBI.
For example: to extract gene sequence "CYTB" from mitogenome in fasta format. Specify the range of gene reported on GenBank for
desired accession number.
./extract_from_mitogenome.py -f fastaFile.fasta -r 14392..15532

For help:
./extract_from_mitogenome.py --help

usage: extract_from_mitogenome.py [-h] -f F -r R

optional arguments:
  -h, --help  show this help message and exit
  -f F        Input file in fasta format
  -r R        Range of the seq to be extracted, GenBank format. e.g., 1..600
