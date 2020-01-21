# -*- coding: utf-8 -*-
"""
leaf name retriever from th Newick file and fasta generator from leaf names

author@islekburak
"""

#libraries
import pandas as pd
from ete3 import Tree
import tkinter as tk
from tkinter import filedialog

#call window to set working directory
root=tk.Tk()
root.withdraw()
directory = filedialog.askdirectory(parent=root,title="Choose directory where you want to put outs")

#call window to select Newick file
root=tk.Tk()
root.withdraw()
path=filedialog.askopenfilename(title="Choose the Newick file that you want to retrieve complete sequences from")

#getting file names from the path
filename=path.split("/")[-1].split(".")[0]

#reading Newick file
t=Tree(path)
leafnamelist=[]
for leaf in t:
	label=leaf.name
	idx=label.find(label.split("|")[3])
	newlabel=label[:idx-1]
	leafnamelist.append(newlabel)

#ask for database of fasta
root=tk.Tk()
root.withdraw()
path=filedialog.askopenfilename()
while path[len(path)-6:]!=".fasta":
	print("Please select the correct database file (i.e. mydb.fasta)")
	path=filedialog.askopenfilename()

#retrieving complete sequences from database that match with the subjects
infile=path
outfile=directory+"/"+"".join(filename)+"_tree_seqs.fasta"
outfile = open (outfile, "w")

found=False
with open (path, "r") as myfasta:
	for line in myfasta:
		if ">" in line and not found:
			for item in leafnamelist:
				if str(item) in line:
					outfile.write(line)
					found=True
					break
		elif ">" in line and found:
			for item in leafnamelist:
				if str(item) in line:
					outfile.write(line)
					found=True
					break
				else:
					found=False
		elif ">" not in line and found:
			outfile.write(line)