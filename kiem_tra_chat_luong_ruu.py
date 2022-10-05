import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import csv
import pandas as pd

Afile = np.loadtxt('./ruu.txt', dtype=float)

# du doan doanh thu voi thuat toan linear regression
# dat bien x hien thi tu cot 1 den cot 11
x = Afile[:, :-1]
y = Afile[:, 11:12]
print("X=",x)
print("\t \b")
print("y=", y)

regression = LinearRegression().fit(x, y)
# fit(x,y) la ham hoi quy tuyen tinh voi x la gia tri dau vao va y la gia tri dau ra

print(
    f"Du doan chat luong ruu: {regression.predict([[7.4,0.7,0,1.9,0.076,11,34,0.9978,3.51,0.56,9.4]])}")

