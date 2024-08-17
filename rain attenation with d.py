import numpy as np
import matplotlib.pyplot as plt
from project import est
def rain():
    f = 10e9
    R = 5
    d = np.arange(1, 101)
    A = np.zeros(len(d))
    for i in range(len(d)):
        A[i] = R * d[i] * est(f)

    plt.figure(3)
    plt.plot(d, A)
    plt.xlabel('distance Km')
    plt.ylabel('A (dB)')
    plt.title('Graph of the rain attenuation as a function of distance.')
    plt.text(20, 20, '{f=10GHz R=5 mm/h}')
    plt.show()

rain()
