import csv
# import pandas as pd
# df = pd.read_csv("./winequality-red.csv")
# df.head()

with open('./winequality-red.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
f.close()
