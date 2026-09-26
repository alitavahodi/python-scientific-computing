import numpy as np

def my_func(x_):
    return np.exp(-x_)*np.sin(x_)

x=np.linspace(0,2*np.pi,100)
y1=my_func(x)

y2=np.exp(-x)*np.sin(x)

print(y1)
print(np.all(y1 == y2))