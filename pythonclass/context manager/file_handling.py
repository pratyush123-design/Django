fo=open("./pratyush.txt","wb")
print("file contents:",fo)
print("Name of the file:",fo.name)
print("Closed or not:",fo.closed)
print("opening mode:",fo.mode)
fo.close()
print("Closed or not:",fo.closed)
print("opening mode :",fo.mode)

