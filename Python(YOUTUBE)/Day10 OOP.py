class Person:
    name="Pratyush"
    age=20
    occupation="Student"

a=Person()
a.name="Ram"
a.age=20
print(a.name,a.age)

class Person:
    name="Pratyush"
    age=20
    occupation="student"
    def info(self):
        print(f"{self.name } is a {self.occupation}")
a=Person()
b=Person()
c=Person()

a.name="Ram"
a.age=29
a.occupation="Officer"
b.name="Hari"
b.age=2
b.occupation="Playyer"
c.name="Shyam"
c.age=30
c.occupation="Teacherr" #if c is removed then it will become default argument

a.info()
b.info()
c.info()


