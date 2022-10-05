import pandas as pd
import numpy as np

Afile = np.loadtxt('./ruu.txt', dtype=float)
# lay du lieu cot 1 den cot 10
x = Afile[:, :10]
y = Afile[:, 10:11]

print(x)
