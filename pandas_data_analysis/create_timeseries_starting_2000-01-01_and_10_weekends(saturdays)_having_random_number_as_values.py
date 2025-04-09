import pandas as pd
import numpy as np

dates=pd.date_range(start='2000-01-01',periods=10,freq='W-SAT')
data=pd.Series(np.random.randint(1,10,10), index=dates)

print(data)
