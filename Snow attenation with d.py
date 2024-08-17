import numpy as np
import matplotlib.pyplot as plt

p = np.array([2.7e-3, 1e-3, 8e-4, 5.8e-4, 4.5e-4, 3.9e-4, 3.3e-4, 2.2e-4, 2.2e-4, 2.2e-4])
R = 5
d = np.arange(1, 101)
lamda = 3

def snow_attenuation():
    A = np.zeros(len(d))

    for i in range(len(d)):
        A[i] = R * d[i] * p[1]

    plt.figure(6)
    plt.plot(d, A)
    plt.xlabel('distance Km')
    plt.ylabel('A (dB)')
    plt.title('Graph of the attenuation as a function of distance')
    plt.text(70, 0.1, '{lamda=3 cm; R=5mm/h}')
    plt.show()

snow_attenuation()