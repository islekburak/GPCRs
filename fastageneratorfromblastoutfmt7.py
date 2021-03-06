# -*- coding: utf-8 -*-
"""
fasta generator & taxid retriever from blast outfmt7 file/s

author@islekburak
"""

#libraries
import os
import itertools
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog

#call window to set working directory
root=tk.Tk()
root.withdraw()
directory = filedialog.askdirectory(parent=root,title="Choose directory where you want to put outs")

#call window to select file/s
root=tk.Tk()
root.withdraw()
paths=filedialog.askopenfilenames(title="Choose the BLAST output file/s that you want to merge with")

#getting file names from the paths
filenames=[]
for i in paths:
	name=i.split("/")[-1].split(".")[0]
	filenames.append(name)

#reading files as dataframe
dfs=[pd.read_csv(i, low_memory=False) for i in paths]
print("The selected files were read")

#ask user to select how many human sequences s/he want as input
root = tk.Tk()
root.withdraw()
number=simpledialog.askstring(title="Input Dialog", prompt="Select range up to (nth) human sequences that you want to analyze:")
intnumber=int(number)

#check it out
print(intnumber)

#getting index of start-end position of dfs and retrieve subjects betwen these indices
idxlist=[]
for i in range(len(dfs)):
	a=(dfs[i][dfs[i]["subject_id"].str.contains("HUMAN")==True].index[0])
	b=(dfs[i][dfs[i]["subject_id"].str.contains("HUMAN")==True].index[intnumber-1])
	idxlist.append(tuple((a,b)))

startlist=[]
endlist=[]
for i in idxlist:
	start=i[0]
	end=i[1]
	startlist.append(start)
	endlist.append(end)

#lists from subjects and concatenate them in a list
concatlistofsubjects=[]
for i in range(len(dfs)):
	dfs[i]=dfs[i].iloc[startlist[i]:endlist[i]+1,1]
	subjectlist=dfs[i].tolist()
	concatlistofsubjects.append(subjectlist)

#unpacking lists in a list	
merged=list(itertools.chain(*concatlistofsubjects))

#remove duplicates
mergedsubjects=[] 
for i in merged: 
    if i not in mergedsubjects: 
        mergedsubjects.append(i)

#creating new data frame with merged subjects (optional)
df=pd.DataFrame(mergedsubjects, columns=["subject_id"])
df.set_index("subject_id", inplace=True)

#df.to_csv("_".join(filenames)+".csv")

#ask for database of fasta
root=tk.Tk()
root.withdraw()
path=filedialog.askopenfilename()
while path[len(path)-6:]!=".fasta":
	print("Please select the correct database file (i.e. mydb.fasta)")
	path=filedialog.askopenfilename()

#retrieving complete sequences from database that match with the subjects
infile=path
outfile=directory+"/"+"_".join(filenames)+"_MSA_input.fasta"
outfile = open (outfile, "w")

found=False
with open (path, "r") as myfasta:
	for line in myfasta:
		if ">" in line and not found:
			for item in mergedsubjects:
				if str(item) in line:
					outfile.write(line)
					found=True
					break
		elif ">" in line and found:
			for item in mergedsubjects:
				if str(item) in line:
					outfile.write(line)
					found=True
					break
				else:
					found=False
		elif ">" not in line and found:
			outfile.write(line)