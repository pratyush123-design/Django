import time
h = int(time.strftime('%H'))
m = int(time.strftime('%M'))
s = int(time.strftime('%S'))
print(h)
print(m)
if(h==0 or h<=11):
    if(m>0 and m<=59):
        if(s>0 and s<=59):
            print("Good Morning")
elif(h>=12 and h<=16):
    if(m>0 and m<=59):
        if(s>0 and s<=59):
            print("Good Afternoon")
elif(h>=17 and h<=21):
    if(m>0 and m<=59):
        if(s>0 and s<=59):
             print("Good Evening")
else:
    print("Good Night")



