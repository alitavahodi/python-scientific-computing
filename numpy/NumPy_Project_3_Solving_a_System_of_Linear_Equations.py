import numpy as np 

A=np.array([[4,0,1,11],
            [3,7,21,0.1],
            [-5,1,0.75,3],
            [13,0,6,2]])

B=np.array([2,1.1,-3,0])

A_varoon=np.linalg.inv(A)

X=np.matmul(A_varoon,B)
print(X)


        