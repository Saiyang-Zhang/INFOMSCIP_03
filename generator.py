from matplotlib import path
from matplotlib.lines import lineStyles
from matplotlib.patches import Polygon

import json
import matplotlib.pyplot as plt
import numpy as np


"""
Random points generator
"""

def generate_points(pt_number, f, polygon):
    in_points = []
    out_points = []
    polygon = path.Path(polygon)

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

def save_points(in_points, out_points, polygon, save_path):
    fig= plt.figure(figsize=(5, 5))
    ax = plt.subplot()

    plt.xlim((0, 10))
    plt.ylim((0, 10))

    plt.xticks([])
    plt.yticks([])

    ax.scatter(in_points[:, 0], in_points[:, 1], s=5, c="blue")
    ax.scatter(out_points[:, 0], out_points[:, 1], s=5, c="red")

    patch = Polygon(polygon)
    patch.set_fill(False)
    ax.add_patch(patch)

    points_dict = dict()
    points_dict["in_points"] = in_points.tolist()
    points_dict["out_points"] = out_points.tolist()

    points_json = json.dumps(points_dict)
    
    points_file = open(save_path+"_points.json", 'w')
    points_file.write(points_json)
    points_file.close()

    plt.savefig(save_path+"_img.png")

"""
Triangle
"""

triangle = [
    [3, 3],
    [7, 3],
    [7, 7]
]

"""
Sample
"""

# in_points, out_points = generate_points(500, 0, triangle)

# save_points(in_points, out_points, triangle, "Sample")

"""
Generate points of different density
"""

# for i in range(8):
#     n = (i+1)*100

#     in_points, out_points = generate_points(n, 0, triangle)

#     save_path = "n/n_"+str(n)

#     save_points(in_points, out_points, triangle, save_path)

"""
Generate points of different fractions of outliers
"""

# for i in range(7):
#     f = round(i*0.05, 2)
    
#     in_points, out_points = generate_points(500, f, triangle)

#     save_path = "f/f_"+str(f)

#     save_points(in_points, out_points, triangle, save_path)

"""
Generate points within triangles of different perimeters
"""

triangles = [
    [[3, 3], [7, 3], [5, 7]],
    [[3, 3], [7, 3], [6, 7]],
    [[3, 3], [7, 3], [7, 7]],
    [[3, 3], [7, 3], [8, 7]],
    [[3, 3], [7, 3], [9, 7]],
    [[2, 3], [6, 3], [9, 7]],
    [[1, 3], [5, 3], [9, 7]]
]

# for i in range(7):
#     t = triangles[i]
    
#     save_path = "d/d_"+str(i)
    
#     in_points, out_points = generate_points(500, 0, t)

#     save_points(in_points, out_points, t, save_path)

"""
Generate $d$ demonstrations
"""

    # in_points, out_points = generate_points(200, 0, t)

    # fig= plt.figure(figsize=(5, 5))
    # ax = plt.subplot()

    # plt.xlim((0, 10))
    # plt.ylim((0, 10))

    # plt.xticks([])
    # plt.yticks([])

    # ax.scatter(in_points[:, 0], in_points[:, 1], s=5, c="blue")
    # ax.scatter(out_points[:, 0], out_points[:, 1], s=5, c="red")

    # line_x0 = [int((t[0][0]+t[1][0])/2), int((t[0][0]+t[1][0])/2)] 
    # line_y0 = [3, 9]
    # line_x1 = [t[2][0], t[2][0]] 
    # line_y1 = [3, 9]
    # line_x2 = [int((t[0][0]+t[1][0])/2), t[2][0]]
    # line_y2 = [3, 3]
    # plt.plot(line_x0, line_y0, color="black", linestyle="--")
    # plt.plot(line_x1, line_y1, color="black", linestyle="--")
    # plt.plot(line_x2, line_y2, color="black", linestyle="--")

    # ax.annotate("", xy=(int((t[0][0]+t[1][0])/2), 8), xytext=(t[2][0], 8),arrowprops=dict(arrowstyle="<->"))
    # plt.text(((t[0][0]+t[1][0])/2+t[2][0])/2, 8.2, "d="+str(int(t[2][0]-int((t[0][0]+t[1][0])/2))), size=12, style="italic")

    # patch = Polygon(t)
    # patch.set_fill(False)
    # ax.add_patch(patch)

    # plt.savefig(save_path+"_img.png")