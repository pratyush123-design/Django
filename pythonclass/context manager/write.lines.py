
lines=["First line\n","Second line \n","Third line \n"]
with open("ram.txt","w") as file:
    file.writelines(lines)
    print("Content added Successfully!!")