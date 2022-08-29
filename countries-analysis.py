import pandas as pd

df = pd.read_csv('datasets/countries.csv')

# Sort by population
sorted_df = df.sort_values(by=['Population'], ascending=False)
least_populated_countries = sorted_df.tail()

# Add a new sample column
least_populated_countries['Nature'] = 'Environment'

for i, row in least_populated_countries.iterrows():
    print(row['Population'])

least_populated_countries.to_csv('least.csv')
