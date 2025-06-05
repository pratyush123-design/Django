# dict={"Name":"Pratyush", "Age":20, "Occupation":"Engineer"}
# print("value is: %s" % dict.has_key("Roll number"))   #shows error
dict={"Name":"Pratyush", "Age":20, "Occupation":"Engineer"}
print("value is: %s" % ("ROll number" in dict))   


dict={"name":"Pratyush","age":3,"cast":"Khatiwada"}
print("my personal info is:",dict)
if "name" in dict:
    print("name is",dict["name"])
else:
    print("{} is not present".format("name") )
if "roll number " in dict:
    print("Roll number is:",dict["Roll number"])
else:
    print("{} is not present in dict".format("Roll number"))


dict={"Animal":"Dog","breed":"German Shephard","Lifespan":20}
print("DOG infor is: ", dict)
if "Animal" in dict:
    print("Animal is:",dict["Animal"])
else:
    print("{} is not in present in dict".format("Animal"))
if "Age" in dict:
    print("Age is:", dict["Age"])
else:
    print("{} is not present in dict".format("Age"))
    