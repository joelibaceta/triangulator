from triangulator.geometry.angles import get_polygon_internal_angle
from triangulator.geometry.points import is_point_inside_triangle

def triangulate(poligon: tuple) -> list:

    final_triangles = []
    vertices = list(poligon)
    original_vertices = list(poligon)
    triangles_finded = -1
    
    # While there are triangles to be found
    while(triangles_finded != 0): 
      triangles_finded = 0
      for index, v in enumerate(vertices):

        prev_vertice = vertices[index - 1]
        next_vertice = vertices[(index + 1) % (len(vertices))]
        vertice = vertices[index]

        vector1 = (vertice[0] - prev_vertice[0], vertice[1] - prev_vertice[1])
        vector2 = (next_vertice[0] - vertice[0], next_vertice[1] - vertice[1])
        
        angle = get_polygon_internal_angle(vector1, vector2)

        if angle >= 180:
            # Skip because angle is greater than 180
            continue
        else:
            triangle = (prev_vertice, vertice, next_vertice)
            points = [p for p in original_vertices if p not in triangle]
            inside_evaluation = [is_point_inside_triangle(triangle, point) for point in points]
            # If are not points inside the triangle
            if True in inside_evaluation:
                # Skip because point is inside triangle
                continue
            else:
                # Add triangle to final triangles
                final_triangles.append(triangle)
                vertices.pop(index)
                triangles_finded += 1
                break
    return final_triangles
