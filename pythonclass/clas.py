class Car:
    def __init__(self,color,model):
        self.color=color #attribute   #self means it calls itself
        self.model=model #attribute
    def honk(self): #method 
        print("Beep beep!")
    def brake(self):
         print("Brake")
    def moredetails(self):
        print(f"{self.model} is a {self.color} color")
#creating an object
my_car=Car("Red","Toyota")
my_car=Car("Yellow","BMW")
my_car.honk()
my_car.brake()
my_car.moredetails()