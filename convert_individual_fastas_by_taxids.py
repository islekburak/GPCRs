#!/usr/bin/env python
from collections import defaultdict

#open file1, using col2 as ids and col1 appending to defaultdict values
with open("ids.txt", "r") as f:
    ids = defaultdict(list)   
    for line in f:
        ids[line.strip().split("\t")[0]].append(line.strip().split("\t")[1])

# open file2 fasta, put sequences into dictionary with col1 ids as keys
with open("outscan_complete_seq_linearized.fasta", "r") as fasta:
    seqs = {}
    for line in fasta:
        if line.startswith(">"):
            seqs[line.strip().split("|")[1]] = next(fasta).strip()

# for each id (used as new filename), print out matching col1 ids and sequences to new file
for i in ids:
    with open(i + ".fasta", "w") as out:
        for n in range(len(ids[i])):
            out.write("\n" + ">" + ids[i][n] + "\n" + seqs[ids[i][n]])
