import numpy as np

ket0 = np.array([[0],[1]])
ket1 = np.array([[1],[0]])

M1 = np.array([[1,1],[0,0]])
M2 = np.array([[1,0],[0,1]])

M = M1 / 2 + M2 / 2


print(np.matmul(M1, ket1))
print(np.matmul(M1, M2))
print(np.matmul(M, M))