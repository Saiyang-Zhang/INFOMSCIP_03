import numpy as np
import matplotlib.pyplot as plt
    # https://stackoverflow.com/questions/22481854/plot-mean-and-standard-deviation


def plot(range, mean, sd, title):
    assert len(range) == len(mean) == len(sd), "arrays are not same length"

    ax = plt.subplot(111)
    ax.errorbar(range, mean, yerr=sd, fmt='-o')
    ax.set_title(title)
    ax.set_xlabel('n')
    plt.show()

def example():
    range = np.arange(100, 900, 100) # upperbound is exclusive
    mean = np.exp(-range)
    sd = 0.1 + 0.2 * range

    plot(range, mean, sd, 'example')
