from ete3 import Tree
t=Tree("iqtree_rooted.treefile")
for leaf in t:
	new_name = leaf.name.split("_")[1]+"_"+leaf.name.split("_")[2]
	leaf.name = new_name
t.write(format=1, outfile="new_tree.nw")