import numpy as np


x = np.full((3, 5), 0, dtype=object)
x[1,1] = (1,1)
print(type(x))
print(x.shape)
print(x.dtype)
print(x)


