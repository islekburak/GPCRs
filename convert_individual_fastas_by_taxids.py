#!/usr/bin/env python
from collections import defaultdict

#open ids.txt, using col2 as taxids and col1 appending to defaultdict values
with open("ids.txt", "r") as f:
    ids = defaultdict(list)   
    for line in f:
        ids[line.strip().split("\t")[0]].append(line.strip().split("\t")[1])

# open linearized fasta file, put sequences into dictionary with col1 ids as keys
# to linearize fasta file before run this command;
# awk '/^>/ {printf("\n%s\n",$0);next; } { printf("%s",$0);}  END {printf("\n");}' < file.fasta > linearized_file.fasta
with open("outscan_complete_seq_linearized.fasta", "r") as fasta:
    seqs = {}
    for line in fasta:
        if line.startswith(">"):
            seqs[line.strip().split("|")[1]] = next(fasta).strip()

# for each taxid (used as new filename), print out matching col1 ids and sequences to new file
for i in ids:
    with open(i + ".fasta", "w") as out:
        for n in range(len(ids[i])):
            out.write("\n" + ">" + ids[i][n] + "\n" + seqs[ids[i][n]])

# to remove first line of new fasta files;
# sed -i '1d' *.fasta
