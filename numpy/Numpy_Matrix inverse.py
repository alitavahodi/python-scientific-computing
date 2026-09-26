#Matrix inverse
import numpy as np
A_mat=np.array([[4,0,1,11],[3,7,21,0.1],[-5,1,0.75,3],[13,0,6,2]])

print(A_mat)
A_inv_mat=np.empty_like(A_mat)
#print(A_inv_mat,A_inv_mat.shape)

for i in range(A_mat.shape[0]):
    for j in range(A_inv_mat.shape[1]):
        temp_A_mat=np.delete(A_mat,i,axis=0)
        temp_A_mat=np.delete(temp_A_mat,j,axis=1)
        A_inv_mat[i,j]=(-1)**(i+j)*np.linalg.det(temp_A_mat)
    
A_inv_mat=A_inv_mat.transpose().conjugate()/np.linalg.det(A_mat)  
print(A_inv_mat)
print(np.linalg.inv(A_mat))
print(A_inv_mat== np.linalg.inv(A_mat))
print(A_inv_mat@ A_mat)
print(np.round(A_inv_mat@ A_mat))


