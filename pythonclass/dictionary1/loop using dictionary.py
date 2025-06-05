
dict={"Name":"Pratyush", "Age":20, "Occupation":"Engineer"}
for key in dict:
    print(key,dict[key])

student={"Name":"Pratyush", "Age":20, "Occupation":"Engineer"}
for key in student:
    print(key,student[key])

#using dict.tems4

student={"Name":"Pratyush", "Age":20, "Occupation":"Engineer"}
for key,value in student.items():
    print(key,value)
#USING DICT.KEYS
student={"Name":"Pratyush", "Age":20, "Occupation":"Engineer"}
for key in student.keys():
    print(key)

#USING VALUES
student={"Name":"Pratyush", "Age":20, "Occupation":"Engineer"}
for value in student.values():
    print(value)