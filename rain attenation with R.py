import numpy as np
import matplotlib.pyplot as plt
from project import est
def rain():
    f = 10e9
    R = np.arange(1, 31)
    d = 50
    A = np.zeros(len(R))
    for i in range(len(R)):
        A[i] = R[i] * d * est(f)

    plt.figure(2)
    plt.plot(R, A)
    plt.xlabel('average of rainfall (mm/h)')
    plt.ylabel('A (dB)')
    plt.title('Graph of the rain attenuation as a function of rainfall.')
    plt.text(5, 60, '{f=10GHz d=50km}')
    plt.show()

rain()
