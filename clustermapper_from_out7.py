# -*- coding: utf-8 -*-
"""
2D-array maker & visualizer from the data of blast outfmt7 outputs hit ranks
author@islekburak
"""

#call window to select file
import tkinter as tk
from tkinter import filedialog
root=tk.Tk()
root.withdraw()
file_path=filedialog.askopenfilename()
#getting file name from the path
name=file_path.split("/")[-1].split(".")[0]
#libraries
import pandas as pd
import scipy.spatial.distance as scidist
from scipy.spatial.distance import squareform
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as scihier
from scipy.cluster.hierarchy import dendrogram, linkage

#reading file
a=pd.read_csv(file_path)
#finding all human hits and indexes
b=a[a["subject_id"].str.contains("HUMAN")==True]
#create lists with hit ranks and subject ids
subjectlist=b.subject_id.tolist()
newsubjectlist=[]
for i in subjectlist:
	gene=i.split("|")[2].split(" ")[0].split("_")[0]
	newsubjectlist.append(gene)
hitranklist=b.index.tolist()
#concatenating lists
data=list(zip(newsubjectlist,hitranklist))
df=pd.DataFrame(data, columns=["subject_id","hit_rank"])
df.set_index("subject_id", inplace=True)
#df.to_csv("final.csv")
dists=scidist.pdist(df,"cityblock")
squareform(dists)
df=pd.DataFrame(squareform(dists), index=[i for i in newsubjectlist], columns= [i for i in newsubjectlist])
df.to_csv("distmatrix_"+name+".csv")
#visualize with seaborn

sns.clustermap(df, metric="correlation", standard_scale=1, figsize=(10,10))
plt.savefig("clustermap_"+name+".png")

"""
x=scihier.linkage(df,"complete")
scihier.dendrogram(x,leaf_rotation=90,leaf_font_size=5, labels=df.index)
plt.savefig("dendrogram1.png")
"""