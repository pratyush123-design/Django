fo = open("foo.txt", "w")
print("Name of the file: ", fo.name)
seq = ["This is the new line", '\n', "This is another new line"]
line = fo.writelines(seq)
print("Check the file to see the reflected changes")
fo.close()