import pandas as pd
import numpy as np
ser = pd.Series(np.random.normal(10, 5, 25))
print(ser.describe().apply(['min','max','25%','75%','std']))

