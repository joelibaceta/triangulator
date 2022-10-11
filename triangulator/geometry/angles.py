import math
import numpy as np

def get_polygon_internal_angle(p1: tuple, p2: tuple):
    return ( math.pi + math.atan2(np.cross(p1, p2), np.dot(p1, p2)) ) * (180/math.pi);