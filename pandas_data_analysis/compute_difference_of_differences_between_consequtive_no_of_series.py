import pandas as pd
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])

diff=ser.diff().tolist()
print(diff)

print(ser.diff().diff().tolist())