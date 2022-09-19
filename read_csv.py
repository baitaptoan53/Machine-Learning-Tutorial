import csv
# doc du lieu tu file csv
with open('./winequality-red.csv') as f:
    reader = csv.reader(f, delimiter='\t')
    x = [row for row in reader]
    y = [row for row in reader]

print(x[1])
# print(y[3:1])