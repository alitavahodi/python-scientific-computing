#MATRIX MULTIPLICATION
import numpy as np

A_matrix=np.linspace(1,20,9).reshape(3,-1)
B_matrix=np.arange(1,7).reshape(3,2)
#print(A_matrix,A_matrix.shape)
#print(B_matrix,B_matrix.shape)
res_shape=(A_matrix.shape[0],B_matrix.shape[1])
#print(res_shape)
res_matrix=np.empty(shape=res_shape)
#print(res_matrix)
for i in range(A_matrix.shape[0]):
    for j in range(B_matrix.shape[1]):
        res_matrix[i,j]=np.dot(A_matrix[i,:],B_matrix[:,j])

print(res_matrix)
print(np.all(res_matrix == A_matrix @ B_matrix))