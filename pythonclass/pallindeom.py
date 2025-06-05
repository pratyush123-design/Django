word = input("Enter word: ") 
word1=word.lower()
if word1==word1[::-1]:
    print(f"'{word}' is a palindrome.")
else: 
    print(f"'{word}' is not a palindrome.")
list=["Level", "madam","Radar"]
for i in list:
    if i.lower()==i.lower()[::-1]:
        print(f"{i} is a palindrome")
    else:
        print(f"{i} is not a palindrome")
        