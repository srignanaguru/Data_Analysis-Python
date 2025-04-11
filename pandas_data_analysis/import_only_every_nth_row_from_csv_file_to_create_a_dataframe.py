import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', chunksize=50)
df2_list = []
for chunk in df:
    df2_list.append(chunk.iloc[0, :])

df2 = pd.DataFrame(df2_list)
print(df2.head())
