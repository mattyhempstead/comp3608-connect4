import pandas as pd

df = pd.read_csv("results.csv")

tab = df.groupby(['a','b']).size()
print(tab)

print(tab / tab.sum())

print(tab.sum())

