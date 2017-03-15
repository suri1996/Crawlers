import pandas as pd

df = pd.read_json('s.json')
df.href.fillna(df.name,inplace=True)
df = df.drop('name',1)

df.to_csv('links.csv', index= False)
