class Person:
    def __init__(self,name,**kwargs):
        super().__init__(**kwargs)
        self.name=name
    def greet (self):
        return f"Hello, my name is {self.name}"
class Employee:
    def __init__(self,employee_id,**kwargs):
        super().__init__(**kwargs)
        self.employee_id=employee_id
    def get_employee_id(self):
        return f"My employee_id is {self.employee_id}"
class Manager (Person,Employee):
    def __init__(self, name,employee_id,department):
        super().__init__(name=name,employee_id=employee_id)
    
        self.department=department
    def show_details(self):
        return f"Hi I am {self.name}, my employee id is {self.employee_id} and my department is {self.department}"
manager=Manager("Patyush","P1234","HR")
print(manager.greet())
print(manager.get_employee_id())
print(manager.show_details())
       
        
class Person:
    def __init__(self,name,):
        
        self.name=name
    def greet (self):
        return f"Hello, my name is {self.name}"
class Employee:
    def __init__(self,employee_id):
        
        self.employee_id=employee_id
    def get_employee_id(self):
        return f"My employee_id is {self.employee_id}"
class Manager (Person,Employee):
    def __init__(self, name,employee_id,department):
        super().__init__(name)
        Employee.__init__(self,employee_id)
        self.department=department
    def show_details(self):
        return f"Hi I am {self.name}, my employee id is {self.employee_id} and my department is {self.department}"
manager=Manager("Patyush","P1234","HR")
print(manager.greet())
print(manager.get_employee_id())
print(manager.show_details())
       
        