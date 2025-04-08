import pandas as pd

my_str = 'dbc deb abed gade'

df=pd.Series(list(my_str))
freq=df.value_counts()
print(freq)

least_freq=freq.dropna().index[-1]
"".join(df.replace(' ', least_freq))
print(least_freq)