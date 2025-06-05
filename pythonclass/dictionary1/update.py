dict={"Name":"Pratyush", "Age":20, "Occupation":"Engineer"}
personal_info=dict.keys()
print(type(personal_info))
print(personal_info)
dict.update({"Status":"Single"})
print(dict)

dict={"Name":"Pratyush", "Age":20, "Occupation":"Engineer"}
personal_info=dict.values()
print(type(personal_info))
dict.update({"class":2})
print(dict)