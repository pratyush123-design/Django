this_dict={
    "Name":"RAM BAHADUR KARKI",
    "Status":"Single",
    "umer": 30
}
print("The this_dict without removing anything is ",this_dict)
del this_dict["Name"]
print("The this_dict after removing name is ", this_dict)


dict={
    "name":"PK",
    "age":20,
    "sex":"M"
}
print("dict before popping is:", dict)
dict.pop("sex")
print("dict after popping is:",dict)
dict.popitem()
print(dict)


dict={
    "Name":"Pratyush",
    "Age": 20, 
    "Profession":"Inspector"
}
dict.clear()
print(dict)


dict={
    "Name":"Pratyush",
    "Age": 20, 
    "Profession":"Inspector"
}
to_remove_keys=["Age", "Profession"] 
for key in to_remove_keys:
    dict.pop(key,None)  #"Using None as the default helps return nothing even if the key_to_remove is not present in the dictionary
print(dict)