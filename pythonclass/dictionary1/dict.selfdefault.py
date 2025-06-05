dict={
    "name":"Pratyush",
    "Age": 20,
    "Job":"Doctor"}
print("value is %s" %  dict.setdefault("sex",None))
print("Value is %s" % dict.setdefault("Age",None))

dict_1 = {'Universe' : {'Planet' : 'Earth'}}
print("The dictionary is: ",dict_1)
# using nested setdefault() method
result = dict_1.setdefault('Universe', {}).setdefault('Planet')
print("The nested value obtained is: ", result)