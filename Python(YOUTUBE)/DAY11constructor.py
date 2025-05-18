class Person:
    def __init__(self, n, o):
        print("I am a Person")
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name } is a{self.occ}")
a=Person("PK","Hr")
# a.name="PK"
# a.occ="HR"
b=Person("OK","HR")
# b.name="OP"
# b.occ="Officer"
a.info()
b.info()


class Person:
    def __init__(self,n,a):
        print("HEy")
        self.name=n
        self.age=a
    def info(self):
         print(f"{self.name} is {self.age} years old")
a=Person("Pk",20)
b=Person("SRK",30)
a.info()
b.info()
