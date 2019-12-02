#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import time


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

#adj_a is now an nxn dataframe matrix, with all entries equal to "False"


#Paul added the following:

#The following code now changes appropriate elements of adj_a to "True"
#These "True" elements indicate the presence of an edge in our network
#This process has a timer also


start = time.process_time() 
for i in range(0,len(df_a_sorted)):
    adj_a[df_a_sorted.iloc[i][0]][df_a_sorted.iloc[i][1]]=True
    
    if i == int(len(df_a_sorted)*.2):
        lap = time.process_time()
        print("20% of adj matrix filled")
        print("Elapsed time = %.2f seconds\n" % (lap-start))
        
    if i == int(len(df_a_sorted)*.4):
        lap = time.process_time()
        print("40% of adj matrix filled")
        print("Elapsed time = %.2f seconds\n" % (lap-start))
        
    if i == int(len(df_a_sorted)*.6):
        lap = time.process_time()
        print("60% of adj matrix filled")
        print("Elapsed time = %.2f seconds\n" % (lap-start))
        
    if i == int(len(df_a_sorted)*.8):
        lap = time.process_time()
        print("80% of adj matrix filled")
        print("Elapsed time = %.2f seconds\n" % (lap-start))
        
    if i == int(len(df_a_sorted)-1):
        lap = time.process_time()
        print("100% of adj matrix filled")
        print("Elapsed time = %.2f seconds\n" % (lap-start))
        
        
end = time.process_time()-start 
print("It took me %.2f seconds "%(end))


#This saves our adj_a dataframe to a csv file on user's computer

adj_a.to_csv("Adj_a.csv", header = False, index = False)
