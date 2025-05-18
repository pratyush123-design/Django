# # class Shape:
# #     def __init__(self,x,y):
# #         self.x=x
# #         self.y=y
# #     def area (self):
# #         return self.x * self.y
# # class Circle(Shape):
# #     def __init__(self,radius):
# #         self.radius=radius
# #         super().__init__(radius,radius)
# #     def area(self):
# #         return 3.14* super().area()
# # rec=Shape(3,4)
# # print(rec.area())
# # C=Circle(5)
# # print(C.area() )

# class Animal:
#     def __init__(self,name):
#         self.name=name
# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.name=name
#         self.breed=breed
# d=Dog("Ramey","Huskey")
# print(d.name,d.breed)
        



# class Parent:
#     def __init__(self,surname):
#         self.surname=surname
# class Child(Parent):
#     def __init__(self,name,surname):
#         super().__init__(surname)
#         self.name=name
# n=Child("Ram","giri")
# n2=Child("hari","Khatiwada")
# # print(f"{n.name} {n.surname}")
# print(f"{n2.name} {n2.surname}")







class Animal():
    def __init__(self,name):
        self.name=name
class Dog(Animal):
    def __init__(self,name,breed,):
        super().__init__(name)
        self.name=name
        self.breed=breed
d=Dog("Ramu","Husker")
print(d.name)