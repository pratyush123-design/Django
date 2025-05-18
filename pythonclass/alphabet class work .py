alphabet=list(input("Enter the strings").split())
print(alphabet)
if len(alphabet)<3:
     print("Thelength of string is less than 3 so ")
     del alphabet
     create_new_alphabet=list(input("Enter another string: ").split())
     print(create_new_alphabet)
else:
     print( "the lenght of alphabet is", len(alphabet), "so the output is", alphabet)

print(len(alphabet))