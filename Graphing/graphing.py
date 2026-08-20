# import numpy as np
# import plotext as plt

# x = np.linspace(0, 5, 1000)
# y = x**2

# plt.plot(x, y)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 10000)
y = x**2 + 3*x + 2

plt.plot(x, y)


plt.grid()
plt.show()