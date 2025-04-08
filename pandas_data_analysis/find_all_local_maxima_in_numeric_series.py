import pandas as pd
import numpy as np
from scipy.signal import find_peaks
ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])

dd = np.diff(np.sign(np.diff(ser)))
peak_locs = np.where(dd == -2)[0] + 1
print(peak_locs)
