import numpy as np
import matplotlib.pyplot as plt

p = np.array([2.7e-3, 1e-3, 8e-4, 5.8e-4, 4.5e-4, 3.9e-4, 3.3e-4, 2.2e-4, 2.2e-4, 2.2e-4])
R = np.arange(1, 31)
d = 50
lamda = 3

def snow_attenuation():
    A = np.zeros(len(R))

    for i in range(len(R)):
        A[i] = R[i] * d * p[1]

    plt.figure(5)
    plt.plot(R, A)
    plt.xlabel('Average of flowing in mm/h')
    plt.ylabel('A (dB)')
    plt.title('Graph of the attenuation as a function of R')
    plt.text(5, 1.2, '{lamda=3 cm; d=50km}')
    plt.show()

snow_attenuation()