import pandas  as pd
import numpy as np

ser = pd.Series(np.arange(20) + np.random.normal(1, 10, 20))

autocorrelations=[ser.autocorr(i).round(2) for i in range(11)]

print(autocorrelations[1:])
print("Lag having highest correlation: ", np.argmax(np.abs(autocorrelations[1:]))+1)