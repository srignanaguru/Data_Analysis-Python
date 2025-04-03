import pandas as pd
import numpy as np
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
value_counts=ser.value_counts()
top_2=value_counts.index[:2]
res=ser.apply(lambda x: x if x in top_2 else 'Other')
print(res)
