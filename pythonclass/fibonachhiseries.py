def fibbonachi(n):
    if n<=1:
        return n 
    
    return fibbonachi(n-1)+fibbonachi(n-2)
limit=10
for num in range(limit):
    print(fibbonachi(num))

     