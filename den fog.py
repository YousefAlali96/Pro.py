import numpy as np
import matplotlib.pyplot as plt
from project import den
x = np.arange(30, 701, 20)

c = np.zeros(len(x))
for i in range(len(x)):
    c[i] = den(x[i])

plt.figure(11)
plt.plot(x, c)
plt.xlabel('eyesight (m)')
plt.ylabel('c (g/m3)')
plt.title('Graph of the fog density as a function of eyesight')
plt.show()