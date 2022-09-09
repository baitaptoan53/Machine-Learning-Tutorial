import matplotlib.pyplot as plt
import numpy as np

y = np.array([99.99,0.01])
mylabels = ["Chim Ngọc", "Chim Vỹ"]

plt.pie(y, labels = mylabels)
plt.legend(title="Bang so sanh do chim to")
plt.show()