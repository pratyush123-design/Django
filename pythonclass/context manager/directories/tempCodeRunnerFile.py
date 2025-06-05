
fo = open("foo.txt", "w+")
print("Name of the file: ", fo.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.readline()
print("Read Line:", line)

# Again set the pointer to the beginning
fo.seek(1, 1)
line = fo.readline()
print("Read Line:", line)

# Close opened file
fo.close()