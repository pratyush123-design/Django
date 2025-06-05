
fo = open("foo.txt", "w")
print("Name of the file: ", fo.name)
str = "This is the new line"
line = fo.write( str )

print("Check the file to see the reflected changes")