import numpy as np
import matplotlib.pyplot as plt
from project import *


x = 30
k = 7e-2
lamda = 3
d = np.arange(1, 51)


A20 = np.zeros(len(d))
A5 = np.zeros(len(d))
AO = np.zeros(len(d))

for i in range(len(d)):
    A20[i] = den(x) * temp20(lamda) * d[i]
    A5[i] = den(x) * temp5(lamda) * d[i]
    AO[i] = k * den(x) * d[i] * 10 / lamda

plt.figure(10)
plt.plot(d, A20, d, A5, '--', d, AO, ':')
plt.xlabel('distance (km)')
plt.ylabel('A (dB)')
plt.title('Graph of the attenuation as a function of distance')
plt.text(8, 100, '{x=30m lamda=3}')
plt.text(40, 20, '{t<Oc}')
plt.text(40, 10, '{t=5c}')
plt.text(40, 5, '{t=20c}')
plt.show()