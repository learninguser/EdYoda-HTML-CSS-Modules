import numpy as np

# question_first_solution
class Circle():
    def __init__(self,radius):
        self.radius = radius
        self.pi = np.math.pi
        
    def getArea(self):
        self.area = self.pi * self.radius ** 2
        return np.round(self.area, 2)

    def getCircumference(self):
        self.circumference = 2 * self.pi * self.radius
        return np.round(self.circumference, 2)
    
    def Display(self):
        return [str(self.getArea()), str(self.getCircumference())]

circle = Circle(1)
print(circle.Display())