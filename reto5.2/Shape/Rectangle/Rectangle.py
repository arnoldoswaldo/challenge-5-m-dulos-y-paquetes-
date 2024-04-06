from Shape.shape import Shape
class Rectangle(Shape):
    def compute_area(self):
        # la multiplicacion de los lados b*h
        return self.edges[0].length * self.edges[1].length

    def compute_perimeter(self):
        # se suma la medida de los lados 
        return 2 * (self.edges[0].length + self.edges[1].length)

    def get_vertices(self):
        return super().get_vertices()

    def set_vertices(self, vertices):
        super().set_vertices(vertices)


class Square(Rectangle):
    def compute_area(self):
        # para el area multiplicamos l*l
        return self.edges[0].length ** 2

    def compute_perimeter(self):
        # sumamos 4 veces la medida del lado  
        return 4 * self.edges[0].length

    def get_vertices(self):
        return super().get_vertices()

    def set_vertices(self, vertices):
        super().set_vertices(vertices)