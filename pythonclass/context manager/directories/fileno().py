# Open a file
fo = open("old.txt", "wb")
print("Name of the file: ", fo.name)

fid = fo.fileno()
print("File Descriptor: ", fid)

# Close opened file
fo.close()