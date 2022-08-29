import pandas as pd

df = pd.read_csv('vgsales.csv')

# Get dataframe info
print(df.info())

# Get column names
print(df.columns)

# Print first 5 rows
print(df.head())

# Print last 5 rows
print(df.tail())

# df = df['Platform'].value_counts().reset_index()
# print('Value ', df)

# Printing in tabular form, tabular package is required
# print(df.to_markdown())

# for index, row in df.iterrows():
#     print(row['Rank'], row['Name'])

# for i, row in df.iloc[:101].iterrows():
#     print(row['Rank'], row['Name'])

gk = df.groupby('Platform').count()
  
# Let's print the first entries
# in all the groups formed.
print(gk)


