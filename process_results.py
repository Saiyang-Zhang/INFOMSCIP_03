import csv
import numpy as np
import graph

def read_results(path):
    mean = []
    std = []
    res = []
    with open(path, 'r') as f:
        read = csv.reader(f)
        for results_str in read:
            if(results_str == []):
                continue
            results = [eval(s) for s in results_str]
            res.append(results)
            mean.append(np.mean(results))
            std.append(np.std(results))
    return (res, mean, std)

(r, m, s) = read_results('results/experiment_1')
graph.errorbar(np.arange(100, 900, 100), m, s, 'Experiment 1', 'n', 'misclassifications', save='ex_1_errorbar')
graph.boxplot(r, np.arange(100, 900, 100), 'Experiment 1', 'n', 'misclassifications', save='ex_1_boxplot')

(r, m, s) = read_results('results/experiment_2')
graph.errorbar(np.arange(0, 0.35, 0.05), m, s, 'Experiment 2', 'f', 'misclassifications', save='ex_2_errorbar')
graph.boxplot(r, np.arange(0, 0.35, 0.05), 'Experiment 2', 'f', 'misclassifications', save='ex_2_boxplot')

(r, m, s) = read_results('results/experiment_3')
graph.errorbar(np.arange(0, 7, 1), m, s, 'Experiment 3', 'd', 'misclassifications', save='ex_3_errorbar')
graph.boxplot(r, np.arange(0, 7, 1),'Experiment 3', 'd', 'misclassifications', save='ex_3_boxplot')
