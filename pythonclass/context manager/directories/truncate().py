
fo = open("foo.txt", "w+")
print("Name of the file: ", fo.name)
line = fo.readline()
print("Read Line:", line)
fo.truncate()
line = fo.readline()
print("Read Line:", line)
fo.close()