import numpy as np
import pandas as pd
mylist=list('abcedfghijklmnopqrstuvwxyz')
myarr=np.arange(26)
mydict=dict(zip(mylist,myarr))

list_series=pd.Series(mylist)
list_arr=pd.Series(myarr)
list_dict=pd.Series(mydict)

print(list_dict.head())
