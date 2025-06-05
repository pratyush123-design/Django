dict={"Name":"Pratyush", "Age":20, "Occupation":"Engineer"}
print("dictionary is", dict.get("roll number"))

dict={"Name":"Pratyush", "Age":20, "Occupation":"Engineer"}
keys_to_Remove=["Name","roll number"]
for key in keys_to_Remove:
    print(dict.pop(key,None))
print(dict)