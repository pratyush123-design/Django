
fo = open("foo.txt", "r+")
print("Name of the file: ", fo.name)

line = fo.readline()
print("Read Line:", line)

fo.close()