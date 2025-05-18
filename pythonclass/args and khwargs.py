
     

class Person:
   def __init__(self,name):
      self.name=name
   def greet(self):
       return f"Hello, my name is {self.name}."

class Employee:
   def __init__(self,employee_id):
      self.employee_id=employee_id
   def get_id(self):
       return f"Hello, employee ID is {self.employee_id}."
class Manager(Person,Employee):
   def __init__(self,name,employee_id,department):
      Person.__init__(self,name)
      Employee.__init__(self,employee_id)
      self.department=department
   def show_details(self):
       return f"{self.greet()} {self.get_id()} I manage the {self.department} department"
manager = Manager("alice", "E1234", "Sales")
print(manager.greet())
      

print(manager.show_details())

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return f"Hello, my name is {self.name}."


# class Employee:
#     def __init__(self, employee_id):
#         self.employee_id = employee_id

#     def get_id(self):
#         return f"Hello, employee ID is {self.employee_id}."


# class Manager(Person, Employee):
#     def __init__(self, name, employee_id, department):
#         Person.__init__(self, name)
#         Employee.__init__(self, employee_id)
#         self.department = department

#     def show_details(self):
#         return f"{self.greet()} {self.get_id()} I manage the {self.department} department."


# # Fixed: added comma between "E1234" and "Sales"
# manager = Manager("alice", "E1234", "Sales")

# print(manager.greet())
# print(manager.show_details())
