class Parent:
    def yormethod(self):       
        print('Calling parent method')
class Child(Parent):
    def Mymethod(self):
        print('Calling child method')
#instance
c=Child()
#child calls overridden method
c.yourmethod()
    

# # class Employee:
# #     def __init__(self,nm,sal):
# #         self.name=nm
# #         self.salary=sal 
# #     def  getName(self):
# #        return self.name
# #     def getSalary(self):
# #        return self.salary 
# # class SalesOfficer(Employee):
# #     def __init__(self,nm,sal,inc):
# #         super().__init__(nm,sal)
# #         self.incnt=inc 
    
# #     def getSalary(self):
# #        return self.salary + self.incnt
# # e1=Employee("Rajesh",9000)
# # print("Total SALAry for {} is Rs{}".format(e1.getName(),e1.getSalary()))
# # s1=SalesOfficer('Kiran',1000,1000)
# # print('Total salary for {} is Rs {}'.format(s1.getName(),s1.getSalary()))


# class Employee:
#     def __init__(self,nm,sal):
#         self.name=nm
#         self.salary=sal 
#     # def getName(self):
#     #     return self.name
#     # def getSalary (self):
#     #     return self.salary
# class SalesOfficer(Employee):
#     def __init__(self,nm,sal,inc):
#         super().__init__(nm,sal)
#         self.inc=inc
#         return 
#     # def getSalary(self):
#     #     return self.salary+self.inc
# e1=Employee("Ram", 30000000)
# print("The salary of {} is {}". format (e1.name,e1.salary))
# s1=SalesOfficer("Hari",10000,10000)
# print("The salary of {} is {}". format (s1.name,s1.salary+s1.inc))