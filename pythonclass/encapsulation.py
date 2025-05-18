# # class Bankaccount:
# #     def __init__(self, balance):
# #         self.__balance=balance #Private attribute
# #     def deposit(self, amount):
# #         self.__balance +=amount
# #     def get_balance(self):
# #         return self.__balance
# # account = Bankaccount(100)
# # account.deposit(50)
# # print(account.get_balance())

# class Student:
#     def __init__(self,name,age):
#         #private method
#         self.name=name
#         self.__age=age 
#     #getter method        
#     def get_age(self):
#         return self.__age
#     #setter method
#     def set_age(self,age):
#         self.age=age
# stud = Student ('jassa',14)
# #retrieving age using getter
# print('Name:',stud.name,stud.get_age())
# #changing age using setter
# stud.set_age(20)
# #retrieving age using getter
# print('Name:',stud.name,stud.get_age())
 


# #excess modifier
# class Employee:
#     def __init__(self,name,age,salary):
#         self.name=name  #public
#         self.__age=age    #private 
#         self.__salary=salary   #protected
#     def displayEmployee(self):
#         print("Name :", self.name,"age:" , self.__age," salary: ", self._salary)
# e1=Employee("Bhavana",24,10000)
# print(e1.name)
# print(e1._salary)
# print(e1.__age)
# print(e1.diplayEmployee())

def add(*nums):
    return sum(nums)
#Call the function with different number of parameters
result1=add(10,20)
result2=add(10,20,30)

print(result1)
print(result2)

