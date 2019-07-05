"""
import pandas as pd
df1=read_csv("scan_out.csv")
df2=read_csv("search_out.csv")
intersected_df=pd.merge(df1,df2,how="inner")
"""


# libraries
from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn2
 
# Make a Basic Venn
v=venn2(subsets = (57, 196, 30), set_labels = ('hmmscan', 'hmmsearch'))
 
# Custom it
v.get_patch_by_id('100').set_alpha(1.0)
v.get_patch_by_id('100').set_color('white')
v.get_label_by_id('100').set_text('scan_outs')
v.get_label_by_id('hmmscan').set_text('Scan_outs')

v.get_patch_by_id('100').set_alpha(1.0)
v.get_patch_by_id('100').set_color('blue')
v.get_label_by_id('100').set_text('57')
v.get_label_by_id('hmmsearch').set_text('Search_outs')

 
# Add title and annotation
plt.title("Domain Quantities from the Results of HMMSearch & HMMScan")
plt.annotate('Domain Set just occured in hmmscan results', xy=v.get_label_by_id('100').get_position() - np.array([0, 0.05]), xytext=(-70,-70),
ha='center', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='gray'))
 
# Show it
plt.show()
