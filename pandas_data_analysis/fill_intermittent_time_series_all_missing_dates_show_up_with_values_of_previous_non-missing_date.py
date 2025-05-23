import pandas as pd
import numpy as np

ser = pd.Series([1,10,3,np.nan], index=pd.to_datetime(['2000-01-01', '2000-01-03', '2000-01-06', '2000-01-08']))

full_range=pd.date_range(start=ser.index.min(), end=ser.index.max(), freq='D')

data_full=ser.reindex(full_range)
data_filled=data_full.ffill()

print(data_filled)