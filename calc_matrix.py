import numpy as np
#create matrix
A =np.array ([[1, 4, 5, 12], 
     [-5, 8, 9, 0], 
     [-6, 7, 11, 19]])
B= np.array([[1, 4, 5, 12],
      [-5, 8, 9, 0], 
     [-6, 7, 11, 19]])
print("A=\n" , A)
print("A[0]=\n", A[0])
print("A[0][1]=\n",A[0][1])
column = []
for b in A:
                   column.append( b[0])
print("column[1]=\n", column)
#cong 2 ma tran
print("A+B=\n",A+B)
#nhan 2 ma tran 
print("A*B=\n",A*B)
#ma tran chuyen vi
print("A^T= \n" ,A.transpose())
C = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
#ma trận nghịch đảo
print("C^-1= \n" , np.linalg.inv(C))

# ma tran duong cheo
print("Ma tran duong cheo" , np.diag(A))