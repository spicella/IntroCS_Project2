

import pandas as pd
import numpy as np

#create the dataframe for the adjacency matrix from output data of Part 2
path="results_WS"
adj_df=pd.read_csv(path+'\data_rewired_n100_r5_p0.300.csv',header=None)  

#plots the probability mass function
x=np.zeros(n)
for i in range(0,n):
    x[i]=sum(adj_df.iloc[i])
plt.hist(x,density=True)
