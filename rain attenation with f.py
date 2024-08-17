import numpy as np
import matplotlib.pyplot as plt
from project import est
def rain():
    R = 5
    d = 50
    f = np.arange(1e9, 301e9, 1e9)
    A = np.zeros(len(f))
    
    for i in range(len(f)):
        A[i] = R * d * est(f[i])
    
    plt.figure(1)
    plt.plot(f, A)
    plt.xlabel('frequency (Hz)')
    plt.ylabel('A (dB)')
    plt.title('Graph of the rain attenuation as a function of freq.')
    plt.text(3, 600, '{R=5mm/h d=50km}')
    plt.show()


rain()
