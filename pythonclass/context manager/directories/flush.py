
fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)

# Here it does nothing, but you can call it with read operation.
fo.flush()

# Close opened file
fo.close()