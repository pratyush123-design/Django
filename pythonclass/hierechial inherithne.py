class Animal:
    def  __init__(self,species):
        self.species=species
    def speak(self):
        return f"{self.species} makes a sound."
class Dog(Animal):
    def  __init__(self,name):
       super().__init__("Dog")
       self.name=name
    def bark(self):
        return f"{self.species} says WOof!."
class Cat(Animal):
    def  __init__(self,name):
       super().__init__("Cat")
       self.name=name
    def meow(self):
        return f"{self.species} says Meow."
dog=Dog("Kukur")
cat=Cat("Biralo")
print(dog.speak())

print(dog.bark())
print(cat.speak())
print(cat.meow())

