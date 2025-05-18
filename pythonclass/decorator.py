def my_function(x):
    
    print("The nummber is = ",x)
def my_decorator(some_function,num):
    def wrapper(num): 
      
        print("Inside wrapper to check odd/ even ")
        
        if num%2==0:
            ret="Even"
        else:
            ret="Odd!"
        some_function(num)
        return ret 
    print("Wrapper function is called")
 
    return wrapper
no=10
my_function=my_decorator(my_function,no)
print("It is", my_function(no))


# def my_decorator(some_function):
#     def wrapper(num): 
       
#         print("Inside wrapper to check odd/ even ")
     
#         if num%2==0:
#             ret="Even"
#         else:
#             ret="Odd!"
#         some_function(num)
#         return ret 
#     print("Wrapper function is called")
#     return wrapper
# @my_decorator
# def my_function(x):
#     print("The number is= ",x)
# no=10
# print("It is ", my_function)

# def hero(heroine):
#     def execute():
#         print("Good Morning")
#         heroine()
#         print("Thank you for using this function ")
#     return execute
# def who_is_Pratyush():
#     print("Pratyush is a good boy ")
# who_is_Pratyush=hero(who_is_Pratyush)
# who_is_Pratyush()


# def hero(Func1):
#     def execute():
#         print("Namaskar")
#         Func1()
#         print("Saiyonara")
#     return execute
# def a():
#     print("Gu")
# a=hero(a)
# a()

# def numbers(x):
#     print("THE NUMBER IS: ",x)
    
# def operators(numbers):
#   def container():
#     print("To store positive or negaative")
#     if numbers<0:
#         print("Negative")
#     else:
#         print("Postive")
#     return container
# a=19
# a=operators(numbers,a)
# a