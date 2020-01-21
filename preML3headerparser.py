# -*- coding: utf-8 -*-
"""
taxid picker (from MSA inputs or outputs) & appender to trimal outs' headers for pre raxml analysis stage

author@islekburak
"""

import tkinter as tk
from tkinter import filedialog

#call window to set working directory
root=tk.Tk()
root.withdraw()
directory = filedialog.askdirectory(parent=root,title="Choose directory where you want to put outs")

#call window to pick taxids (MSA input)
root=tk.Tk()
root.withdraw()
path=filedialog.askopenfilename(title="Choose the MSA input file to retrieve Taxids")

#create taxid list from MSA file
taxidlist=[]
with open(path,"r") as firstfasta:
	for line in firstfasta:
		if line[0]==">":
			taxstart=line.find("OX=")
			taxend=line.find(" ",taxstart)
			taxid=line[taxstart+3:taxend]
			taxidlist.append(taxid)

#call window to select file (trimal output)
root=tk.Tk()
root.withdraw()
path2=filedialog.askopenfilename(title="Choose the Trimal output file that you want to parse")

#getting file names from the path
filename=path2.split("/")[-1].split(".")[0]


outfile=directory+"/"+"".join(filename)+"_preML3.fasta"
outfile = open (outfile, "w")

with open (path2, "r") as secondfasta:
	for line in secondfasta:
		if line.startswith (">"):
			line = line[1:] # skip the ">" character
			header=line.split(" ")[0]
			headerroot=header.split("_")[0]
			organism=header.split("_")[1]
			for item in taxidlist:
				finalheader=">"+headerroot+"|"+organism+"|"+item
			outfile.write (finalheader + "\n")
		else:
			outfile.write(line)
outfile.close()
