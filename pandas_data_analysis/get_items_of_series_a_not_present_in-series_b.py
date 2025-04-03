import pandas as pd

ser1= pd.Series([1,2,3,4,5])
ser2= pd.Series([4,5,6,7,8])

res=ser1[~ser1.isin(ser2)]
print(res)
