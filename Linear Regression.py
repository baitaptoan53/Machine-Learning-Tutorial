from __future__ import print_function , division , unicode_literals
import numpy as np
import  matplotlib.pyplot as plt

x=np.array([[147,150,153,158,163,165,168,170,175,173,178,180,183]]).T

y= np.array([[49,50,51,54,58,59,60,62,63,64,66,67,68]]).T

plt.plot(x,y,'ro')
plt.axis([140,190,45,75])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

one = np.ones((x.shape[0],1))
Xbar = np.concatenate((one,x),axis=1)

A=np.dot(Xbar.T,Xbar)
b=np.dot(Xbar.T,y)
w=np.dot(np.linalg.pinv(A),b)
print('w = ',w)

w_0 = w[0][0]
w_1= w[1][0]
x0 = np.linspace(145,185,2)
y0 = w_0 + w_1*x0

plt.plot(x.T,y.T,'ro')
plt.plot(x0,y0)

plt.show()