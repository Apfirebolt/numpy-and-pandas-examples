import pandas as pd
import time

start_time = time.time()

# df = pd.read_csv('news.csv', chunksize=100000)

# df_chunked = pd.read_csv("news.csv", chunksize=100000)
df_chunked = pd.read_csv("datasets/vgsales.csv", chunksize=1000, names=['Name'])
# df = pd.read_csv("vgsales.csv")

# for index, row in df.iterrows():
#     print(row)


for chunk in df_chunked:
    for index, row in chunk.iterrows():
        print(row)

print("--- %s seconds ---" % (time.time() - start_time))


