dict={"Name":"Pratyush", "Age":20, "Occupation":"Engineer"}
for key in dict.items():
    print(key)
   
dict={"Name":"Pratyush", "Age":20, "Occupation":"Engineer"}
x=dict.items()
print ("The dictionary is: ", x )
dict['RollNo'] = 37
print ("The dictionary view-object is: ", x)