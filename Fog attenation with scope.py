import numpy as np
import matplotlib.pyplot as plt
from project import *

k = 7e-2
x = np.array([30, 60, 90, 128, 150, 200, 300, 500, 640])
lamda = 3
d = 50


A2O = np.zeros(len(x))
A5 = np.zeros(len(x))
AO = np.zeros(len(x))

for i in range(len(x)):
    A2O[i] = den(x[i]) * temp20(lamda) * d
    A5[i] = den(x[i]) * temp5(lamda) * d
    AO[i] = k * den(x[i]) * d  / lamda
plt.figure(8)
plt.plot(x, A2O, label='A20')
plt.plot(x, A5, '--', label='A5')
plt.plot(x, AO, ':', label='AO')
plt.xlabel('eyesight (m)')
plt.ylabel('A (dB)')
plt.title('Graph of the attenuation as a function of eyesight')
plt.text(300, 10, '{lamda=3cm d=50km}')
plt.text(50, 0.5, '{t<0c}')
plt.text(100, 7, '{t=5c}')
plt.text(200, 2, '{t=20c}')
plt.legend()
plt.show()