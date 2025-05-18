class example:
    def add(self, a= None, b=None, c=None):
        x=0
        if a !=None and b!=None and c!=None:
            x=a+b+c
        elif a !=None and b!=None and c==None:
            x=a+b
        else:
            x=a
            print(x)
obj = example()
print(obj.add(10,20,30))    #yesko kam sakkepaxi yo print hudaina
print(obj.add(10))
