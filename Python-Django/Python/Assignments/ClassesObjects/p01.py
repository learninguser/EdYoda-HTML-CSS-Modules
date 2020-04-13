import math
class Circle():
    def __init__(self,radius):
      self.radius = radius
      self.pi = 3.14159265359
      
    def getArea(self):
        self.area = self.pi * self.radius ** 2
        return round(self.area, 1)

    def getCircumference(self):
        self.circumference = 2 * self.pi * self.radius
        return round(self.circumference, 1)
    
    def Display(self):
        return [str(self.getArea()) + '0', str(self.getCircumference()) + '0']

circle = Circle(5)
print(circle.Display())