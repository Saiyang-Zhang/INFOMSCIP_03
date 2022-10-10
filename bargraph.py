import random
import numpy as np
import matplotlib.pyplot as plt

def plotbar(range, mean, std, title):
    assert len(range) == len(mean) == len(std)

    x_pos = np.arange(len(range))

    # Build the plot
    fig, ax = plt.subplots()
    ax.bar(x_pos, mean, yerr=std, align='center', alpha=0.5, ecolor='black', capsize=10)
    ax.set_ylabel('Mean values of the repeats')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(range)
    ax.set_title('Bar Graph with Mean & STD')
    ax.yaxis.grid(True)

    # Save the figure and show
    plt.tight_layout()
    #plt.savefig('bar_plot_with_error_bars.png')
    plt.show()

def example():
    range = np.arange(100, 900, 100)
    mean = np.arange(50, 450, 50)
    std = 0.1 + 0.2 * range

    plotbar(range, mean, std, 'example')

example()