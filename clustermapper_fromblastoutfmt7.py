# -*- coding: utf-8 -*-
"""
2D-array maker & visualizer from the data of blast outfmt7 outputs hit ranks
author@islekburak
"""

#libraries
import os
import pandas as pd
import tkinter as tk
import seaborn as sns
import scipy.spatial as sp
from tkinter import filedialog
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
import scipy.spatial.distance as distance
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import dendrogram, linkage

#call window to set working directory
root=tk.Tk()
root.withdraw()
directory =filedialog.askdirectory(parent=root,title="Choose directory where you want to put outs")

#call window to select file
root=tk.Tk()
root.withdraw()
file_path=tk.filedialog.askopenfilename(title="Choose the BLAST output file that you want to cluster")

#getting pwd
pwd=file_path.rsplit("/", 1)[0]

#getting file name from the path
name=file_path.split("/")[-1].split(".")[0]

#reading file
a=pd.read_csv(file_path)

#finding all human hits and indexes
b=a[a["subject_id"].str.contains("HUMAN")==True]

#indexlist=a[a.iloc([i]["subject_id"]).str.contains("HUMAN")==True

#create lists with hit ranks and subject ids
subjectlist=b.subject_id.tolist()
newsubjectlist=[]
for i in subjectlist:
	gene=i.split("|")[2].split(" ")[0].split("_")[0]
	newsubjectlist.append(gene)

hitranklist=b.index.tolist()

frame=b.loc[b.index.isin(hitranklist)]
idscorelist=frame.identity.tolist()

#alignmentlengthlist=frame.alignment_length.tolist()

#bitscorelist=frame.bit_score.tolist()

#concatenating lists
data=list(zip(newsubjectlist,hitranklist,idscorelist))
df1=pd.DataFrame(data, columns=["subject_id","hit_rank","id_score"])
df1.set_index("subject_id", inplace=True)
df1.to_csv(directory+"/"+"data_of_"+name+".csv")

#calculating distances between every dots
dists=distance.pdist(df1,"euclidean",w=2)

#create 2D matrix data
squareform(dists)

#create 2D matrix file
df=pd.DataFrame(squareform(dists), index=[i for i in newsubjectlist], columns= [i for i in newsubjectlist])

#new_directory=pwd+"/"+name+"_outs/"

#os.mkdir(new_directory)
df.to_csv(directory+"/"+"distmatrix_"+name+".csv")

#visualize with seaborn
"""
plt.title("Hierarchically Clustered Heatmap with Dendogram for "+name)
plt.xlabel("Target Sequences (Only Human)")
plt.ylabel("Distances")
"""
sns.heatmap(df, cmap="Spectral")
plt.savefig(directory+"/"+"heatmap_"+name+".png")
plt.close()

sns.clustermap(df, method="average", metric="euclidean", standard_scale=1, cmap="Spectral" , figsize=(10,10))
plt.savefig(directory+"/"+"clustermap_"+name+".png")
plt.close()

y=sch.linkage(df1,"centroid")
sch.dendrogram(y,leaf_rotation=90,leaf_font_size=5, labels=df1.index)
plt.savefig(directory+"/"+"dendrogram_"+name+".png")
plt.close()
