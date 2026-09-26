import numpy as np

a1=np.array([-1.2,3.8,5])
a2=np.array([4.1,0,2.2])
a1_dot_a2=np.dot(a1,a2)
a1_mag=np.sqrt((a1**2).sum())
a2_mag=np.sqrt((a2**2).sum())
theta=np.arccos(a1_dot_a2/(a1_mag*a2_mag))
print(np.rad2deg(theta))
print((np.cross(a1,a2)**2).sum()**0.5)