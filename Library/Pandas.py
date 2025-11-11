import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())
df['new_column'] = df['existing_column'] * 2
df.to_csv("data_modified.csv", index=False)
