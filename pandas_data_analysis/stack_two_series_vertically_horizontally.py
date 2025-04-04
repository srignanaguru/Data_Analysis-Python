import pandas as pd
import numpy as np

ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

#Vertical
res=pd.concat([ser1,ser2],axis=0)
print(res)
#Horizontal
res=pd.concat([ser1,ser2],axis=1)
print(res)
