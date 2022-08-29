import pandas as pd

columns = ['Name', 'Genre']

df = pd.read_csv('vgsales.csv', usecols=columns)

df.to_csv('compressed.csv')

# Print first 5 rows
print(df.head())

# Print last 5 rows
print(df.tail())