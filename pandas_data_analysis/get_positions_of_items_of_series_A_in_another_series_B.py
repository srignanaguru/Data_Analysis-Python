import pandas as pd
import numpy as np
ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])

res=[pd.Index(ser1).get_loc(i) for i in ser2]
print(res)

