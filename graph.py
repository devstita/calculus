import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__': 
    x = np.linspace(-5, 5, 100000)
    y  = x ** 2

    plt.plot(x, y)
    plt.show()
