#from experiments import repeat_experiment
import experiments as exp
import csv

triangle = [
    [3, 3],
    [7, 3],
    [7, 7]
]

path = 'results/'

with open('results/experiment_1', 'w') as f:
    for i in range(8):
        results = exp.repeat_experiment(100 + i * 100, 0, triangle)
        write = csv.writer(f)
        write.writerow(results)
   
with open('results/experiment_2', 'w') as f:
    for i in range(7):
        results = exp.repeat_experiment(500, i * 0.05, triangle)
        write = csv.writer(f)
        write.writerow(results)


triangles = [
    [[3, 3], [7, 3], [5, 7]],
    [[3, 3], [7, 3], [6, 7]],
    [[3, 3], [7, 3], [7, 7]],
    [[3, 3], [7, 3], [8, 7]],
    [[3, 3], [7, 3], [9, 7]],
    [[2, 3], [6, 3], [9, 7]],
    [[1, 3], [5, 3], [9, 7]]
]
with open('results/experiment_3', 'w') as f:
    for i in range(7):
        results = exp.repeat_experiment(500, 0, triangles[i])
        write = csv.writer(f)
        write.writerow(results)

    