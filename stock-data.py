import pandas as pd

df = pd.read_csv('GAIL.csv')

# New column in dataframe which is formed by the difference in consecutive rows.
df['Percentage Change'] = df['Prev Close'] - df['Prev Close'].shift(-1)

# Print and convert column names to a list.
print(df.columns.to_list())

print(df.head())