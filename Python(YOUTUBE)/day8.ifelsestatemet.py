a=int(input("Enter your age:"))
print("Your age is:",a)
if a>=18:
    print("You can drive")
else:
    print("You cannot drive")

#  elif
appleprice = int(input("Enter the price of apple:"))
if(appleprice<50):
    print("Alexa, add 1 kg apple to carts")
elif(appleprice<100):
    print("Warning! LOW BUDGET")
else:
    print("Dont buy")

num=float(input("Enter the number:"))
print("Your number is :", num)
if(num<0):
    print("It is negative")
elif(num==0):
    print("num is zero")
else:
    print("It is positive")
print("Huuray!")

#Nested if else
num=int(input("Enter the Number:"))
if (num<0):
    print("Number is negative")
elif(num>0):
    if(num==0):
        print("It is even")
    elif(num!=0):
        print("It is odd")
else:
    print("Number is zero")

