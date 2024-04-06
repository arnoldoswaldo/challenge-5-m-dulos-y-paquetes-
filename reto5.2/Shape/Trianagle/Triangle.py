from Shape.shape import Shape
from Line.Line import Line
class Triangle(Shape):
    def __init__(self, vertices, inner_angles):
        super().__init__(vertices, inner_angles)
        self.type = self.determine_type()

    def determine_type(self):
        a, b, c = sorted([edge.length for edge in self.edges])
        # tolerancia de error (1e-6) para comparar las longitudes de los lados.
        if abs(a ** 2 + b ** 2 - c ** 2) < 1e-6:
            return "Rectangulo"
        elif a == b == c:
            return "Equilatero"
        elif a == b or b == c:
            return "Isosceles"
        else:
            return "Escaleno"

    def compute_area(self):
        a, b, c = sorted([edge.length for edge in self.edges])
        if self.type == "Rectangulo":
            # Para un triangulo rectangulo, el área es (base * altura)/2
            return 0.5 * a * b
        elif self.type == "Isósceles":
            # Para un triángulo isósceles, el area es base * raiz cuadrada((lado^2) - (base^2 / 4)) / 2
            base = a if a != b else c
            side = b if a == b else a
            return base * ((side ** 2 - (base ** 2 / 4)) ** 0.5) / 2
        elif self.type=="Equilatero":
            #Para un tirangulo equilatero calculamos el area con ((raizcuadrada 3)/) * lado al cuadrado
            a = self.edges[0].length
            return ((3 ** 0.5) / 4) * a ** 2
        else:
            # Para un triángulo escaleno, utilizamos la formula de Heron donde s=semiperimetro
            s = (a + b + c) / 2
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def compute_perimeter(self):
        # La suma de los lados
        return sum(edge.length for edge in self.edges)
    
class EquilateralTriangle(Triangle):
    def __init__(self, vertices, inner_angles):
        super().__init__(vertices, inner_angles)

    def compute_area(self):
        # Área de un triángulo equilátero
        a = self.edges[0].length
        return ((3 ** 0.5) / 4) * a ** 2

    def get_vertices(self):
        return super().get_vertices()

    def set_vertices(self, vertices):
        super().set_vertices(vertices)


class RectangleTriangle(Triangle):
    def __init__(self, vertices, inner_angles):
        super().__init__(vertices, inner_angles)

    def compute_area(self):
        # area de un triángulo rectangulo
        a = self.edges[0].length
        b = self.edges[1].length
        return 0.5 * a * b

    def get_vertices(self):
        return super().get_vertices()

    def set_vertices(self, vertices):
        super().set_vertices(vertices)


class ScaleneTriangle(Triangle):
    def __init__(self, vertices, inner_angles):
        super().__init__(vertices, inner_angles)

    def compute_area(self):
        # Usando la fórmula de Heron
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def get_vertices(self):
        return super().get_vertices()

    def set_vertices(self, vertices):
        super().set_vertices(vertices)


class IsoscelesTriangle(Triangle):
    def __init__(self, vertices, inner_angles):
        super().__init__(vertices, inner_angles)

    def compute_area(self):
        # area de un triángulo isosceles
        a, b, c = sorted([edge.length for edge in self.edges])
        base = a if a != b else c
        side = b if a == b else a
        return base * ((side ** 2 - (base ** 2 / 4)) ** 0.5) / 2

    def get_vertices(self):
        return super().get_vertices()

    def set_vertices(self, vertices):
        super().set_vertices(vertices)