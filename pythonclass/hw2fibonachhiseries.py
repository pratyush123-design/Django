def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n)
i1=0
i2=1
limit=10
count=0
while count<limit:
    b=i1+i2
    print(b)
    i1=i2
    b=i2
    count+=1
    print(f"factoiral of fibonachhi number {b} is:  {factorial(b)}")
