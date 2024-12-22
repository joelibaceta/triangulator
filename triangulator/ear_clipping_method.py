import numpy as np
import math
def signed_area(polygon):
    """Calculate the signed area of a polygon to determine its winding order."""
    area = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % len(polygon)]
        area += (x1 * y2 - x2 * y1)
    return area / 2

def ensure_winding_order(polygon):
    """Ensure that the polygon vertices are in counter-clockwise order."""
    if signed_area(polygon) < 0:
        polygon.reverse()  # Reverse if the order is clockwise
    return polygon
def calculate_clockwise_angle(a, b, c):
    """
    calculate the counterclockwise angle between two vectors BA and BC
    Args:
        a, b, c (tuple): 2D coords of triangle vertices (x, y)
    Returns:
        float: counterclockwise angle in degrees
    """
    # vector BA and BC
    ba = np.array([a[0] - b[0], a[1] - b[1]])
    bc = np.array([c[0] - b[0], c[1] - b[1]])
    
    # cross product and magnitude
    dot_product = np.dot(ba, bc)
    magnitude_ba = np.linalg.norm(ba)
    magnitude_bc = np.linalg.norm(bc)
    
    # calculate cos(theta)
    cos_theta = dot_product / (magnitude_ba * magnitude_bc)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)  # avoid invalid value
    angle = np.degrees(np.arccos(cos_theta))
    
    # check the direction of the angle
    cross_product = ba[0] * bc[1] - ba[1] * bc[0]
    if cross_product > 0:
        # anticlockwise angle
        angle = 360 - angle
    
    return angle
def is_point_in_triangle(a, b, c, p):
    """
    check if point P is inside triangle ABC
    Args:
        a, b, c (tuple): vertices of the triangle, format (x, y)
        p (tuple): pt to be checked, format (x, y)
    Returns:
        bool: True -> inside or on boundaries，False -> outside
    """
    # convert to numpy array
    a, b, c, p = map(np.array, [a, b, c, p])
    
    # calculate vectors
    ab = b - a
    ap = p - a
    bc = c - b
    bp = p - b
    ca = a - c
    cp = p - c

    # cross product
    cross1 = np.cross(ab, ap)
    cross2 = np.cross(bc, bp)
    cross3 = np.cross(ca, cp)

    # check the sign of the cross product
    return (cross1 >= 0 and cross2 >= 0 and cross3 >= 0) or (cross1 <= 0 and cross2 <= 0 and cross3 <= 0)
def triangulate(polygon: tuple) -> list:
    """
    This function will triangulate any polygon and return a list of triangles.

        Parameters: 
            polygon (tuple): A tuple of tuples with the points of the polygon
        Returns:
            list: A list of tuples with the triangles vertices
    """

    final_triangles = []
    vertices = list(polygon)
    original_vertices = list(polygon)
    triangles_found = -1

    # Ensure the winding order is counter-clockwise
    vertices = ensure_winding_order(vertices)

    # While there are triangles to be found
    while triangles_found != 0: 
        triangles_found = 0

        for index, _ in enumerate(vertices):
            prev_vertex = vertices[index - 1]
            next_vertex = vertices[(index + 1) % len(vertices)]  # using mod to avoid index out of range
            vertex = vertices[index]

        
            angle = calculate_clockwise_angle(prev_vertex, vertex, next_vertex)

            if angle >= 180:
                # Skip because angle is greater than or equal to 180
                continue
            else:
                # Build a triangle with the three vertices
                triangle = (prev_vertex, vertex, next_vertex)
                # Get vertices that are not part of the triangle
                points = [p for p in original_vertices if p not in triangle]
                # Check if there is a vertex inside the triangle using barycentric coordinates
                inside_evaluation = [is_point_in_triangle(prev_vertex,vertex,next_vertex, point) for point in points]
                # If no points are inside the triangle
                if not any(inside_evaluation):
                    # Add triangle to final triangles
                    final_triangles.append(triangle)
                    # Remove vertex from vertices
                    vertices.pop(index)
                    # Increment triangles found
                    triangles_found += 1
                    break

        # Check for infinite loop
        if triangles_found == 0:
            print(f"Loop detected. Exiting. found {len(final_triangles)} triangles")
            break

    return final_triangles