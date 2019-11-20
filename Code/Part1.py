#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


file_path = "/Users/sergiopicella/Downloads/ca-GrQc.txt"
df_a = pd.read_csv(file_path,delimiter="\t",header=None)
df_a = df_a.rename(columns={0:"from", 1:"to"})

df_a_sorted = df_a.sort_values(by=["from"])
df_a.shape

n = df_a.nunique(axis=0)[0]
ordered_a_indices = np.arange(0,n,1,dtype='int')
ordered_a_indices
print(len(ordered_a_indices))

ordered_a_list = df_a_sorted["from"].unique()
ordered_a_list
len(ordered_a_list)

for j in range(0,n):
    df_a = df_a.replace(ordered_a_list[j],ordered_a_indices[j]) 
df_a_sorted = df_a.sort_values(by=['from'])

adj_a = pd.DataFrame(np.zeros(shape=[n,n]),dtype='bool')
#adj_a

