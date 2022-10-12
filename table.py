import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def create(headerLabel, headers, mean, std, save):
    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    # Convert to array
    headers = np.array(np.around(headers, 2))
    mean = np.array(np.around(mean, 2))
    std = np.array(np.around(std, 2))

    # Reshape data to fit a row instead of column
    headers.reshape(-1, len(headers))
    mean.reshape(-1, len(mean))
    std.reshape(-1, len(std))

    data = np.vstack((headers, mean, std))
    df = pd.DataFrame(columns=headers, data=data)

    ax.table(
        cellText=df.values, 
        rowLabels=[headerLabel, 'mean', 'std'],
        rowColours=['0.8'] * len(mean),
        loc='center')

    fig.tight_layout()
    plt.savefig("figures/" +save, dpi=300)

def example():
    headers=np.array(['age','gender','height',
     'weight','ap_hi','ap_lo',
     'chol','gluc','smoke',
     'alco','active'])

    mean = np.array([35,2,160,56,120,80,1,1,0,0,1])
    std = np.array([35,2,160,56,120,80,1,1,0,0,1])
    create('test', headers, mean, std, "test")