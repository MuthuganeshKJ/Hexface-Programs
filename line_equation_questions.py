import numpy as np
import matplotlib.pyplot as plt
import numpy as np

a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
x = (np.linalg.solve(a, b))
print(np.array(x))