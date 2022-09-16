import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
# import pandas as pd
data = pd.read_csv('./winequality-red.csv', sep=';')
data.head()
# Để tính hồi quy tuyến tính cho dữ liệu mình sẽ sử dụng hàm LinearRegression của thư viện scikit learn đã import ở trên
X_train = data.iloc[:, :-1].values
y_train = data.iloc[:, 1:11].values
regression = LinearRegression()
regression.fit(X_train, y_train)
plt.show()

print('Chat luong ruu la',regression.predict(np.array([[7.4,0.7,0,1.9,0.076,11,34,0.9978,3.51,0.56,9.4]])))