# Open a file
fo = open("foo.txt", "r")
print("Name of the file: ", fo.name)

line1 = fo.read()
line2=fo.read()
print("Read Line: ", line1)
print("Read Line: ", line2)

# Close opened file
fo.close()