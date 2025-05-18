# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @property
#     @abstractmethod
#     def sound(self):
#         pass
# class Bird(Animal):
#     @property
    
#     def sound(self):
#         return"Chirp"
# bird=Bird()
# print(bird.sound)


from abc import ABC, abstractmethod
class Car(ABC):
    @property
    @abstractmethod
    def speed(self):
        pass
class Bugati(Car):
    @property
    def speed(self):
        return "Suiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
bugati=Bugati()
print(bugati.speed)


from abc import ABC, abstractmethod
class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    
    def __init__(self,radius):
        self.radius=radius
    @property
    def area(self):
        return 3.14*self.radius*self.radius
    @property
    def perimeter(self):
        return 2*3.14*self.radius
circle=Circle(10)
print(f"the area of cirlce is {circle.area}")
print(f"the perimeter of cirlce is {circle.perimeter}")
