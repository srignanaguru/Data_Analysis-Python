import pandas as pd
import numpy as np

ser = pd.Series(np.random.randint(1, 10, 7))
print(ser)
res=ser[ser%3==0].index.tolist()
print(res)