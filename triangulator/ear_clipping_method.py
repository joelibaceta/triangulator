from triangulator.geometry.angles import get_polygon_internal_angle
from triangulator.geometry.points import is_point_inside_triangle_barycentric

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

            # Get Vector from prev_vertex to vertex
            vector1 = (vertex[0] - prev_vertex[0], vertex[1] - prev_vertex[1])
            # Get Vector from vertex to next_vertex
            vector2 = (next_vertex[0] - vertex[0], next_vertex[1] - vertex[1])
            # Get internal angle
            angle = get_polygon_internal_angle(vector1, vector2)

            if angle >= 180:
                # Skip because angle is greater than or equal to 180
                continue
            else:
                # Build a triangle with the three vertices
                triangle = (prev_vertex, vertex, next_vertex)
                # Get vertices that are not part of the triangle
                points = [p for p in original_vertices if p not in triangle]
                # Check if there is a vertex inside the triangle using barycentric coordinates
                inside_evaluation = [is_point_inside_triangle_barycentric(triangle, point) for point in points]
                # If no points are inside the triangle
                if True in inside_evaluation:
                    # Skip because a point is inside the triangle
                    continue
                else:
                    # Add triangle to final triangles
                    final_triangles.append(triangle)
                    # Remove vertex from vertices
                    vertices.pop(index)
                    # Increment triangles found
                    triangles_found += 1
                    break

    return final_triangles