from abc import ABC, abstractmethod

class shapes(ABC):
    
    @abstractmethod
    def area(self):
        pass

class circle(shapes):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
class square(shapes):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side **2
    
class pizzaa(circle):
    def __init__(self, radius, toppings):
        super().__init__(radius)
        self.toppings = toppings

shapes = [circle(5), square(3), pizzaa(8, "Chilli")]

for shape in shapes:
    print(f"the area is {shape.area()}cm²")