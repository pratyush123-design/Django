with open("ram.txt","w") as file:
    file.write("Hello, world!")
    print("Content added Successfully!!")


file = open("example.txt", "a")
file.write("Appending this line.\n")
file.close()
print ("File opened successfully!!")