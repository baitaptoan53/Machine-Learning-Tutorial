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

df = pd.read_csv('winequality-red.csv')

print(df.to_string()) 

# du doan doanh thu voi thuat toan linear regression
#dat bien a hien thi tu cot 1 den cot 11 
x = Afile[:, :10]
y = Afile[:, 11:12]
print(x)
print("\t \b")
print("y=", y)
# w = np.linalg.pinv(x @ x.T) @ x @ y
# print("W=", w)
regression = LinearRegression().fit(x, y)

print(f"Du doan doanh thu: {regression.predict([[5, 700]])}")
# print(f"coefficient of determination: {regression.score(x, y)}")

# print(f"intercept: {regression.intercept_}")
# print(f"slope: {regression.coef_}")