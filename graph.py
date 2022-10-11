import numpy as np
import matplotlib.pyplot as plt
    # https://stackoverflow.com/questions/22481854/plot-mean-and-standard-deviation


def errorbar(range, mean, sd, title, xlabel='', ylabel='', show=False, save=''):
    assert len(range) == len(mean) == len(sd), "arrays are not same length"

    fig= plt.figure(figsize=(6, 5))

    ax = plt.subplot(111)
    ax.errorbar(range, mean, yerr=sd, fmt='o', capsize=6, capthick=2)
    plt.ylim((0, max(mean) + max(sd)*1.2))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.yaxis.grid(True)
    if show:
        plt.show()
    if save != '':
        plt.savefig("figures/" + save)

def boxplot(data, range, title, xlabel='', ylabel='', show=False, save=''):
    fig, ax = plt.subplots(figsize=(6,5))
    ax.boxplot( data, 
                widths=.6, 
                patch_artist=True,
                showmeans=False, 
                showfliers=True,
                medianprops={"color": "white", "linewidth": 2},
                boxprops={"facecolor": "C0", "edgecolor": "white",
                          "linewidth": 0.5},
                whiskerprops={"color": "C0", "linewidth": 1.5},
                capprops={"color": "C0", "linewidth": 2},
                flierprops={"markerfacecolor": "C0", "markeredgecolor" : "C0"})

    ax.set_xticklabels(np.around(range, 2))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.yaxis.grid(True)
    if show:
        plt.show()
    if save != '':
        plt.savefig("figures/" + save)

def example():
    range = np.arange(100, 900, 100) # upperbound is exclusive
    mean = np.arange(50, 450, 50)
    sd = 0.1 + 0.2 * range

    errorbar(range, mean, sd, 'example')

#example()