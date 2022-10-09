from ast import List
from matplotlib import path
from matplotlib.patches import Polygon
import generator as gen
import numpy as np

# constants
repeat = 5
q_size = 10000
k_nn = 5

# Performs a single experiment. Repeats it 20 times.
# Args:
# n: Amount of points in base set S
# f: Fractional percentage of outliers in base set S
# poly: Triangular separator used for classifying the points
# repeat: Number of times the experiment will be repeated
# returns: A list with the amount of misclassifications per repeat as integers
def repeat_experiment(n, f, poly_points):
    misses = []

    poly = path.Path(poly_points)
    # perform a single repeat of the experiment
    for i in range(repeat):
        # generate base set S
        # returns array with pairs of (point, classification) (hopefully)
        S_in, S_out = gen.generate_points(n, f, poly_points)
        S = np.concatenate((S_in, S_out))
        S_in_classes = np.repeat([True], len(S_in))
        S_out_classes = np.repeat([False], len(S_out))
        S_classes = np.concatenate((S_in_classes, S_out_classes))

        # generate 10000 points and test them against base set S
        miss = 0
        for j in range(q_size):
            if(j % 1000 == 0):
                print("Repeat " + str(i) + ", q_point: " + str(j))
            point = np.random.rand(2,1) * 10
            actual_class = poly.contains_point(point)
            knn_class = kNN(k_nn, point, S, S_classes)
            if actual_class != knn_class:
                miss += 1

        misses.append(miss)

    return misses

# Performs k-Nearest-Neighbour classification with point p on base set S
# returns: classification of p based on its k nearest neighbours in S
def kNN(k, p, S, classes):
    dists = []
    for i in range(len(S)):
        # figure out the distance squared to point p and add to list with classification
        s = S[i]
        dist = (p[0] - s[0]) * (p[0] - s[0]) + (p[1] - s[1]) * (p[1] - s[1])
        dists.append((dist, classes[i]))

    # custom sort on first element of tuple, which is the distance
    # now the first k elements are the closest ones
    closest_points = sorted(dists, key=lambda x:x[0])

    # count the amount of inside and outside points from the k closest points
    inside = 0
    outside = 0
    for i in range(k):
        clas = closest_points[i][1]
        if closest_points[i][1]:
            inside += 1
        else:
            outside += 1

    return (inside >= outside)


# temp
triangle = [
    [3, 3],
    [7, 3],
    [7, 7]
]
# pointsin, pointsout = gen.generate_points(500, 0, triangle)
# print(np.concatenate((pointsin, pointsout)))
# print(np.repeat([True], len(pointsin)))
print(repeat_experiment(100, 0, triangle))