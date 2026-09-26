import numpy as np 

A=np.array([0,1])

for i in range(20): 
    B=A[-1]+A[-2]
    A=np.concatenate((A,[B]))
print(A)

        