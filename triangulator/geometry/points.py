def is_point_inside_triangle(triangle: tuple, point: tuple) -> bool:
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