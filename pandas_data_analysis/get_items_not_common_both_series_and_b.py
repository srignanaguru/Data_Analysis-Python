import pandas as pd

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

res=pd.concat([ser1,ser2]).drop_duplicates(keep=False)

print(res)
