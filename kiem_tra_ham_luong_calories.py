import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# doc du lieu tu file
# doc du lieu tu file csv
# def read_data(filename):
#                    data = np.genfromtxt(filename, delimiter=',')
#                    return data

Afile = np.loadtxt('./bang_du_lieu_ve_calories.text', dtype=int)

# du doan doanh thu voi thuat toan linear regression
# dat bien a hien thi tu cot 1 den cot 11
x = Afile[:, 1:4]
y = Afile[:, :1]
# print("x=",x)
# print("\t \b")
# print("y=", y)
# w = np.linalg.pinv(x @ x.T) @ x @ y
# print("W=", w)
regression = LinearRegression().fit(x, y)


def mean_squared_error(act, pred):

    diff = pred - act
    differences_squared = diff ** 2
    mean_diff = differences_squared.mean()

    return mean_diff

act = np.array([120, 5, 6, 11])
pred = np.array([105.03438044, 5, 6, 11])
print("Ham mat mat:",mean_squared_error(act, pred))
print(f"Ham luong calories: {regression.predict([[5,6,11]])}")
# print(f"coefficient of determination: {regression.score(x, y)}")

# print(f"intercept: {regression.intercept_}")
# print(f"slope: {regression.coef_}")
