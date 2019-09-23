#!/usr/bin/env python
from collections import defaultdict

#open file1, using col3 as ids and col2 appending to defaultdict values
with open('file_1.txt', 'r') as f:
    ids = defaultdict(list)   
    for line in f:
        ids[line.strip().split('\t')[1]].append(line.strip().split('\t')[2])

# open file2 fasta, put sequences into dictionary with col2 ids as keys
with open('file_2.fasta', 'r') as fasta:
    seqs = {}
    for line in fasta:
        if line.startswith('>'):
            seqs[line.strip().split('|')[1]] = next(fasta).strip()

# for each id (used as new filename), print out matching col2 ids and sequences to new file 
for i in ids:
    with open(i + '.fasta', 'w') as out:
        for n in range(len(ids[i])):
            out.write('>' + ids[i][n] + '\n' + seqs[ids[i][n]])