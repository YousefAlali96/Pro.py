import numpy as np
import matplotlib.pyplot as plt
from project import *
lamda = np.array([1, 2,3,4,5,7, 10])

B20 = np.zeros(len(lamda))
B5 = np.zeros(len(lamda))

for i in range(len(lamda)):
    B20[i] = temp20(lamda[i])
    B5[i] = temp5(lamda[i])

plt.figure(12)
plt.plot(lamda, B20, lamda, B5, ':')
plt.text(2, 0.7, 't=20')
plt.text(1, 0.1, 't=5')
plt.xlabel('lamda (cm)')
plt.ylabel('bita')
plt.title('Graph of bita as a function of lambda')
plt.show()