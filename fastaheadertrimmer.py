# -*- coding: utf-8 -*-
"""
to change fasta headers:
author@islekbro

"""

infile="3_6.fasta"
outfile="3_6_parsed.fasta"
outfile = open (outfile, "w")
with open (infile, "r") as myfasta:
    for line in myfasta:
        if line.startswith (">"):
            line = line[1:] # skip the ">" character
            protein=line.split("|")[1]
            gene=line.split("|")[2].split(" ")[0].split("_")[0]
            organism=line.split("|")[2].split(" ")[0].split("_")[1]
            taxstart=line.find("OX=")
            taxend=line.find(" ",taxstart)
            taxid=line[taxstart+3:taxend]
            finalheader=protein+"|"+gene+"|"+organism+"|"+taxid
            outfile.write ( ">"+finalheader + "\n")
        else:
            outfile.write(line)
outfile.close()
