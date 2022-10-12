import csv
import numpy as np
import graph
import table

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
n = np.arange(100, 900, 100)
graph.errorbar(n, m, s, 'Experiment 1', 'n', 'misclassifications', save='ex_1_errorbar')
graph.boxplot(r, n, 'Experiment 1', 'n', 'misclassifications', save='ex_1_boxplot')
table.create('n', n, m, s, save='ex_1_table')

(r, m, s) = read_results('results/experiment_2')
f = np.arange(0, 0.35, 0.05)
graph.errorbar(f, m, s, 'Experiment 2', 'f', 'misclassifications', save='ex_2_errorbar')
graph.boxplot(r, f, 'Experiment 2', 'f', 'misclassifications', save='ex_2_boxplot')
table.create('f', f, m, s, save='ex_2_table')

(r, m, s) = read_results('results/experiment_3')
d = np.arange(0, 7, 1)
graph.errorbar(d , m, s, 'Experiment 3', 'd', 'misclassifications', save='ex_3_errorbar')
graph.boxplot(r, d ,'Experiment 3', 'd', 'misclassifications', save='ex_3_boxplot')
table.create('d', d, m, s, save='ex_3_table')
