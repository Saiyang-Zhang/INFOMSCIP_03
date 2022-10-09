import csv
import numpy as np
import graph

def read_results(path):
    mean = []
    std = []
    with open(path, 'r') as f:
        read = csv.reader(f)
        for results_str in read:
            if(results_str == []):
                continue
            results = [eval(s) for s in results_str]
            mean.append(np.mean(results))
            std.append(np.std(results))
    return (mean, std)

(m, s) = read_results('results/experiment_1')
graph.plot(np.arange(100, 900, 100), m, s, 'experiment 1')

(m, s) = read_results('results/experiment_2')
print(m, s)
(m, s) = read_results('results/experiment_3')
print(m, s)