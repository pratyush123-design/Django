class Animal:
    def __init__(self,species):
       self.species=species
    def eat(self):
       return f" {self.species} eats "
class Dog(Animal):
    def __init__(self, species,name):
        super().__init__(species)
        self.name=name
    def bark(self):
        return f"{self.name} barks"
class Juvenile_dog(Dog):
    def __init__(self,species,name,age):
        super().__init__(species, name)
        self.age=age
    def size (self):
         return f"{self.age} So, it is a Juvenile dog"
class Puppy(Dog,Animal):
    def __init__(self,species,name,size):
        super().__init__(species,name)
        self.size=size
    def small(self):
        return f"{self.size} So it, is a small puppy"
class Cat(Animal):
    def __init__(self,species,meow):
        super().__init__(species)
        self.meow=meow
    def meow (self):
        return f"{self.meow} is a cat"
dog=Dog("Canis lupus", "Kukur")
puppy=Puppy("Canis lupus","Setey","2 inch ")
cat=Cat("Felis catus", "meow")
juvenile_dog=Juvenile_dog("Canis lupus", "Kukur","2 years ")
print(dog.bark())
print(puppy.eat())
print(cat.eat())
print(puppy.small())
print(juvenile_dog.size())