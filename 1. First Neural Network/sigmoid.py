import numpy as np 

x = -0.558

m = 1 / (1 + np.exp(-x))

y = 0.36

y1 = y * (1 - y)
print("\nAnswer")
print(y1)