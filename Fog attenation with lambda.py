import numpy as np
import matplotlib.pyplot as plt
from project import *


k = 7e-2
d = 50
lamda = np.array([1, 2, 3, 4, 5, 7, 10])

x = 30

A20 = np.zeros(len(lamda))
A5 = np.zeros(len(lamda))
AO = np.zeros(len(lamda))

for i in range(len(lamda)):
    A20[i] = den(x) * temp20(lamda[i]) * d
    A5[i] = den(x) * temp5(lamda[i]) * d
    AO[i] = k * den(x) * d *10 / lamda[i]

plt.figure(9)
plt.plot(lamda, A20, lamda, A5, '--', lamda, AO, ':')
plt.xlabel('lamda (cm)')
plt.ylabel('A (dB)')
plt.title('Graph of the attenuation as a function to wave length')
plt.text(8, 100, '{x=30m d=50km}')
plt.text(6, 20, '{t<0c}')
plt.text(3, 20, '{t=5c}')
plt.text(1.5, 10, '{t=20c}')
plt.show()