class Circle:
  def __init__(self,radius):
    self.radius = radius
  def Area(self):
    return 3.14*(self.radius**2)
  def display_area(self):
    print("the area of the circle is:",self.Area())

  def Perimeter(self):
    return 2*3.14*self.radius
  def display_perimeter(self):
    print("the perimeter of the circle is",self.Perimeter())


r = int(input("radius: "))
circle = Circle(r)
circle.display_area()
circle.display_perimeter()