
from Point.Point import Point
from Line.Line import Line as Line
import Shape
from Shape.Trianagle.Triangle import Triangle, RectangleTriangle, ScaleneTriangle, IsoscelesTriangle, EquilateralTriangle
from Shape.Rectangle.Rectangle import Rectangle, Square

def main ():
    p1 = Point(0, 0)
    p2 = Point(0, 2)
    p3 = Point(11, 11)

    # Crea un triángulo y determina su tipo
    triangle = Triangle(vertices=[p1, p2, p3], inner_angles=[p1, p2, p3])
    triangle_type = triangle.type
    print("Tipo de triángulo:", triangle_type)

    # Dependiendo del tipo de triángulo, crea una instancia de la clase correcta
    if triangle_type == "Rectángulo":
        triangle = RectangleTriangle(vertices=[p1, p2, p3], inner_angles=[p1, p2, p3])
    elif triangle_type == "Isosceles":
        triangle = IsoscelesTriangle(vertices=[p1, p2, p3], inner_angles=[p1, p2, p3])
    elif triangle_type == "Equilatero":
        triangle = EquilateralTriangle(vertices=[p1, p2, p3], inner_angles=[p1, p2, p3])
    elif triangle_type == "Escaleno":
        triangle = EquilateralTriangle(vertices=[p1, p2, p3], inner_angles=[p1, p2, p3])

    # Calcula e imprime el area y el perímetro del triangulo
    print("Área del triángulo:", triangle.compute_area())
    print("Perímetro del triángulo:", triangle.compute_perimeter())

    # Para el rectángulo y el cuadrado, el código permanece igual
    rectangle = Rectangle(vertices=[p1, Point(5, 0), Point(5, 3), Point(0, 3)], inner_angles=[p1, Point(5, 0), Point(5, 3), Point(0, 3)])
    print("Área del rectángulo:", rectangle.compute_area())
    print("Perímetro del rectángulo:", rectangle.compute_perimeter())

    square = Square(vertices=[p1, Point(3, 0), Point(3, 3), Point(0, 3)], inner_angles=[p1, Point(3, 0), Point(3, 3), Point(0, 3)])
    print("Área del cuadrado:", square.compute_area())
    print("Perímetro del cuadrado:", square.compute_perimeter())

if __name__ == "__main__":
  main() 


