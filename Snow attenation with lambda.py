import numpy as np
import matplotlib.pyplot as plt

p = np.array([2.7e-3, 1e-3, 8e-4, 5.8e-4, 4.5e-4, 3.9e-4, 3.3e-4, 2.2e-4, 2.2e-4, 2.2e-4])
R = 5
d = 50
lamda = np.arange(1, 11)

def snow_attenuation():
    A = np.zeros(len(lamda))

    for i in range(len(lamda)):
        A[i] = R * d * p[i]

    plt.figure(1)
    plt.plot(lamda, A)
    plt.xlabel('lamda (cm)')
    plt.ylabel('A (dB)')
    plt.title('Graph of the attenuation as a function of lamda')
    plt.text(7, 0.1, '{R=5mm/h; d=50km}')
    plt.show()

snow_attenuation()