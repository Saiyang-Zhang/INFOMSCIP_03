from matplotlib import path
from matplotlib.patches import Polygon

import matplotlib.pyplot as plt
import numpy as np


"""
Random points generator
"""

def generate_points(pt_number, f, polygon):
    in_points = []
    out_points = []
    for i in range(pt_number):
        point = np.random.rand(2,1)
        point *= 10
        if polygon.contains_point(point):
            in_points.append(point)
        else:
            out_points.append(point)
    
    in_points = np.array(in_points)
    out_points = np.array(out_points)
    
    if(f != 0):
        num_in_outliers = int(f*len(in_points))
        num_out_outliers = int(f*len(out_points))
        
        np.random.shuffle(in_points)
        np.random.shuffle(out_points)

        in_outliers = in_points[:num_in_outliers, :]
        out_outliers = out_points[:num_out_outliers, :]

        in_points = np.vstack((in_points[num_in_outliers:, :], out_outliers))
        out_points = np.vstack((out_points[num_out_outliers:, :], in_outliers))
    
    return in_points, out_points

"""
Data writer
"""

def save_points(in_points, out_points, save_path):
    fig= plt.figure(figsize=(5, 5))
    ax = plt.subplot()

    plt.xlim((0, 10))
    plt.ylim((0, 10))

    plt.xticks([])
    plt.yticks([])

    ax.scatter(in_points[:, 0], in_points[:, 1], s=5, c="blue")
    ax.scatter(out_points[:, 0], out_points[:, 1], s=5, c="red")

    patch = Polygon([a, b, c])
    patch.set_fill(False)
    ax.add_patch(patch)

    # plt.show()    
    np.save(save_path+"in.npy", in_points)
    np.save(save_path+"out.npy", out_points)
    plt.savefig(save_path+"img.png")

"""
Triangle
"""

a = [3, 3]
b = [7, 3]
c = [7, 7]

triangle = path.Path([a, b, c])

"""
Sample
"""

in_points, out_points = generate_points(500, 0, triangle)

save_points(in_points, out_points, "Sample_")

"""
Generate points of different density
"""

# for i in range(8):
#     n = (i+1)*100

#     in_points, out_points = generate_points(n, 0, triangle)

#     save_path = "n/n_"+str(n)

#     save_points(in_points, out_points, save_path)

"""
Generate points of different fractions of outliers
"""

# for i in range(7):
#     f = round(i*0.05, 2)
    
#     in_points, out_points = generate_points(500, f, triangle)

#     save_path = "f/f_"+str(f)

#     save_points(in_points, out_points, save_path)

"""
Generate points within triangles of different perimeters
"""

# triangles = [
#     [[3, 3], [7, 3], [, 7]],
#     [[3, 3], [7, 3], [, 7]],
#     [[3, 3], [7, 3], [, 7]],
#     [[3, 3], [7, 3], [, 7]],
#     [[3, 3], [7, 3], [, 7]],
#     [[3, 3], [7, 3], [, 7]],
#     [[3, 3], [7, 3], [, 7]]
# ]

# triangles = [
#     [[, ], [, ], [, ]],
#     [[, ], [, ], [, ]],
#     [[, ], [, ], [, ]],
#     [[, ], [, ], [, ]],
#     [[, ], [, ], [, ]],
#     [[, ], [, ], [, ]],
#     [[, ], [, ], [, ]]
# ]

# for i in range(7):

#     in_points, out_points = generate_points(500, triangle)
    
#     fig= plt.figure(figsize=(5, 5))
#     ax = plt.subplot()

#     plt.xlim((0, 10))
#     plt.ylim((0, 10))

#     plt.xticks([])
#     plt.yticks([])

#     ax.scatter(in_points[:, 0], in_points[:, 1], s=5, c="blue")
#     ax.scatter(out_points[:, 0], out_points[:, 1], s=5, c="red")

#     patch = Polygon([a, b, c])
#     patch.set_fill(False)
#     ax.add_patch(patch)

#     # plt.show()    
#     np.save("./p/p_"+str(f)+"_in.npy", in_points)
#     np.save("./p/p_"+str(f)+"_out.npy", out_points)
#     plt.savefig("./p/p_"+str(f)+"_img.png")
