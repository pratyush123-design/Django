#POLYMORPHISM
#duck typing
class Duck:
    def sound(self):
        return "Quack,quack!"
class AnotherBird:
    def sound(self):
        return "I am similar to a duck"
def makeSound (duck):
    print(duck.sound())
#creating instances
duck=Duck()
anotherBird=AnotherBird()
#calling mehtods
makeSound(duck)
makeSound(anotherBird)

class Animal:
    alive = True
class dog(Animal):
    def speak(self):
        print("Bark")
class cat(Animal):
    def speak(self):
         print("MEow")
class car:
    alive=False
    def speak(self):
        print("PEEP PEEP!")

Animals=[dog(),cat(),car()]
for animal in Animals:
  animal.speak()

#METHOD OVERRIDING
# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def draw(self):  #super classs or parent class
#         print("Abstract method")
#         return 
# class circle(shape):
#     def draw(self):
#         super().draw()
#         print("Draw a circle")

#         return 
# # class rectangle(shape):
# #     def draw(self):
# #         super().draw()
# #         print("Draaw rectangle")
# #         return
# # shape=[circle(), rectangle()]
# # for shp in shape:
# #     shp.draw()

# #OVERLOADING IN PYTHON
# class Vector:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __str__(self):
#         return 'Vector (%d,%d)' % (self.a,self.b)
#     def __add__(self,other):
#         return Vector(self.a+ other.a,self.b+ other.b)
# v1=Vector(2,10)
# v2=Vector(5,-2)
# print(v1+v2)

# def add(*nums):
#     return sum(nums)
# #Call the function with different number of parameters
# result1=add(10,20)
# result2=add(10,20,30)

# print(result1)
# print(result2)