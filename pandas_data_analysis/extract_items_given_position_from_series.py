import pandas as pd
import numpy as np

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

res=ser.iloc[pos]
print(res)