import math
from Line.Line import Line

class Shape:
    def __init__(self, vertices, inner_angles):
        self.vertices = vertices
        self._inner_angles = inner_angles
        self.edges = [Line(vertices[i], vertices[(i + 1) % len(vertices)]) for i in range(len(vertices))]
        self._inner_angles = self.compute_inner_angles()
        self.is_regular = self.compute_is_regular()

    def compute_inner_angles(self):
        angles = []
        for i in range(len(self.vertices)):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % len(self.vertices)]
            p3 = self.vertices[(i + 2) % len(self.vertices)]
            angle = self.compute_angle(p1, p2, p3)
            angles.append(angle)
        return angles

    def compute_angle(self, p1, p2, p3):
        d1 = p1.compute_distance(p2)
        d2 = p2.compute_distance(p3)
        d3 = p3.compute_distance(p1)
        numerator = d1 ** 2 + d3 ** 2 - d2 ** 2
        denominator = 2 * d1 * d3
        # Manejar divisiones por cero
        if denominator == 0:
            return 0
        # Calcular el ángulo utilizando teorema de coseno
        angle_rad = math.acos(numerator / denominator)
        # Convertir radianes a grados
        angle_deg = angle_rad * 180 / math.pi
        return angle_deg

    def compute_is_regular(self):
        return len(set(self._inner_angles)) == 1

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, vertices):
        self._vertices = vertices

    def get_inner_angles(self):
        return self._inner_angles

    def set_inner_angles(self, inner_angles):
        self._inner_angles = inner_angles
