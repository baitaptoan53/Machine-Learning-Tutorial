from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

# area
x1 = np.array([[60, 40, 100]]).T
# so phong ngu
x2 = np.array([[2, 2, 3]]).T
# cach trung tam
x3 = np.array([[10, 5, 7]]).T
# input matrix X
X = np.concatenate([x1, x2, x3], axis=1)

# price
y = np.array([[10, 12, 20]]).T

plt.plot(X, y)
plt.ylabel('price')
plt.xlabel('area, so phong ngu, cach trung tam')
# fit the model by Linear Regression
# fit_intercept = False for calculating the bias
regr = linear_model.LinearRegression(fit_intercept=True)

regr.fit(X, y)

# Compare two results
print('Coefficient : ', regr.coef_)
print('Interception  : ', regr.intercept_)

plt.show()