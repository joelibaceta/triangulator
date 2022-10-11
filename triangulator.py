import enum
import math
import numpy as np
import matplotlib.pyplot as plt


polygon = ((1, 1), (4, 2), (3, 2), (2, 7), (3, 4), (7, 3), (8, 3), (9, 0))

final_triangles = []


def internal_angle(p1: tuple, p2: tuple):
    return ( math.pi + math.atan2(np.cross(p1, p2), np.dot(p1, p2)) ) * (180/math.pi);

def is_inside_triangle(triangle: tuple, point: tuple) -> bool:
    A, B, C = triangle
    P = point
    Ax, Ay = A
    Bx, By = B
    Cx, Cy = C
    Px, Py = P

    def area(x1, y1, x2, y2, x3, y3):
      return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

    Area1 = area(Ax, Ay, Bx, By, Cx, Cy)
    Area2 = area(Px, Py, Bx, By, Cx, Cy)
    Area3 = area(Ax, Ay, Px, Py, Cx, Cy)
    Area4 = area(Ax, Ay, Bx, By, Px, Py)

    return Area1 == Area2 + Area3 + Area4
 
def triangles(poligon: tuple) -> list:

    vertices = list(poligon)
    original_vertices = list(poligon)

    triangles_finded = -1
    
    while(triangles_finded != 0):
      triangles_finded = 0
      for index, v in enumerate(vertices):

          print(list(vertices))

          if index == 0:
              continue
          else:

            prev_vertice = vertices[index - 1]
            next_vertice = vertices[(index + 1) % (len(vertices))]
            vertice = vertices[index]

            vector1 = (vertice[0] - prev_vertice[0], vertice[1] - prev_vertice[1])
            vector2 = (next_vertice[0] - vertice[0], next_vertice[1] - vertice[1])
            
            angle = internal_angle(vector1, vector2)
            
            print(f"({prev_vertice}, {vertice}, {next_vertice})")
            print(f"Angle: {angle}")

            if angle >= 180:
                print("Skip because angle is greater than 180")
                continue
            else:
                triangle = (prev_vertice, vertice, next_vertice)
                points = [p for p in original_vertices if p not in triangle]
                inside_evaluation = [is_inside_triangle(triangle, point) for point in points]
                print(f"Inside evaluation: {inside_evaluation}")
                if True in inside_evaluation:
                    print("Skip because point is inside triangle")
                    continue
                else:
                    print("Triangle: ", triangle)
                    final_triangles.append(triangle)
                    vertices.pop(index)
                    triangles_finded += 1
                    break


triangles(polygon)

from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

polygon1 = Polygon(polygon)

fig, ax = plt.subplots(1,1)

ax.add_patch(polygon1)

plt.ylim(0,9)
plt.xlim(0,9)

for triangle in final_triangles:
    edge1 = (triangle[0], triangle[1])
    edge2 = (triangle[1], triangle[2])
    edge3 = (triangle[2], triangle[0])
    plt.plot(*zip(*edge1), color='red')
    plt.plot(*zip(*edge2), color='green')
    plt.plot(*zip(*edge3), color='yellow')
plt.show()
