# -*- coding: utf-8 -*-
"""
2D-array maker & visualizer from the data of blast outfmt7 outputs' similarity using clustal omega global alignment
author@islekburak
"""

#libraries
import pandas as pd
import tkinter as tk
import seaborn as sns
from tkinter import filedialog
import matplotlib.pyplot as plt
from Bio.Align.Applications import ClustalOmegaCommandline

#call window to set working directory
root=tk.Tk()
root.withdraw()
directory =filedialog.askdirectory(parent=root,title="Choose directory where you want to put outs")

#call window to select file
root=tk.Tk()
root.withdraw()
file_path=filedialog.askopenfilename(title="Choose the BLAST output file that you want to clustero")

#getting pwd
pwd=file_path.rsplit("/", 1)[0]

#getting file name from the path
name=file_path.split("/")[-1].split(".")[0]

#reading file
a=pd.read_csv(file_path)

#finding all human hits and indexes
b=a[a["subject_id"].str.contains("HUMAN")==True]

#create lists with hit ranks and subject ids
subjectlist=b.subject_id.tolist()

mergedsubjects=[] 
for i in subjectlist: 
    if i not in mergedsubjects: 
        mergedsubjects.append(i)

#ask for database of fasta
root=tk.Tk()
root.withdraw()
path=filedialog.askopenfilename(title="Please select the database file")
while path[len(path)-6:]!=".fasta":
	print("Please select the correct database file (i.e. mydb.fasta)")
	path=filedialog.askopenfilename()

#retrieving complete sequences from database that match with the subjects
infile=path
outfile=directory+"/"+"".join(name)+".fasta"
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
outfile.close()

outfile=directory+"/"+name+".fasta"

#using fasta sequences for MSA (clustalo-globalalignment)
in_file = outfile
out_file = directory+"/"+"".join(name)+"aligned.fasta"
mat_file = directory+"/"+"".join(name)+".mat"
dnd_file = directory+"/"+"".join(name)+".dnd"

#clustalo -i x.fasta --distmat-out=x.mat --guidetree-out=x.dnd -o x.aln --outfmt=clustal -v --full
clustalomega_cline = ClustalOmegaCommandline(infile=in_file, distmat_out=mat_file, guidetree_out=dnd_file, outfile=out_file, outfmt="clustal", verbose=True, distmat_full=True)

#print(clustalomega_cline)
clustalomega_cline()


infile=open(mat_file,"r")
out=open(directory+"/"+name+"_revised.mat","w")

next(infile)
for i in infile:
	first=i.split()[0].split("|")[2].split("_")[0]
	others=i.split()[1:]
	string= ",".join(others)
	string2=first+","+string
	out.write(string2+"\n")
out.close()


df=pd.read_csv(directory+"/"+name+"_revised.mat", header=None)

headers=df.iloc[:,0].tolist()

df2=df.set_index(list(df)[0])
df2.columns=[i for i in headers]
df2.to_csv(directory+"/"+name+"_revised.mat")


#using matrix file for create heatmap
df=pd.read_csv(directory+"/"+name+"_revised.mat")
df=df.set_index("0")
del df.index.name

sns.heatmap(df, cmap="viridis")
plt.savefig(directory+"/"+name+"_heatmap.png")
plt.close()

sns.clustermap(df, method="average", metric="euclidean", standard_scale=1, cmap="Spectral" , figsize=(10,10))
plt.savefig(directory+"/"+name+"_clustermap.png")
plt.close()

"""
y=sch.linkage(df1,"centroid")
sch.dendrogram(y,leaf_rotation=90,leaf_font_size=5, labels=df1.index)
plt.savefig(directory+"/"+"dendrogram_"+name+".png")
plt.close()
"""