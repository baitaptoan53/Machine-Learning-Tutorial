import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import csv
import pandas as pd
# doc du lieu tu file
#doc du lieu tu file csv 
# def read_data(filename):
#                    data = np.genfromtxt(filename, delimiter=',')
#                    return data
# doc du lieu tu file csv
def read_data(filename):              
                   data = pd.read_csv(filename)
                   return data
print(read_data('./winequality-red.csv'))
Afile = np.loadtxt('./bang_doanh_thu.txt',dtype=int) 

# du doan doanh thu voi thuat toan linear regression
#dat bien a hien thi tu cot 1 den cot 11 
x = Afile[:, :2]
y = Afile[:, 2:3]
print(x)
print("\t \b")
print("y=", y)
# w = np.linalg.pinv(x @ x.T) @ x @ y
# print("W=", w)
regression = LinearRegression().fit(x, y)

print(f"Chat luong ruu: {regression.predict([[2,3]])}")
# print(f"coefficient of determination: {regression.score(x, y)}")

# print(f"intercept: {regression.intercept_}")
# print(f"slope: {regression.coef_}")