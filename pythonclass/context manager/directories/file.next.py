fo = open("foo.txt", "r")
print ("Name of the file: ", fo.name )
for index in range(5):
   line = next(fo)
   print ("Line No %d - %s" % (index+1, line.strip()))
fo.close()
print ("Line No %d - %s" % (index+1, line.strip()))
fo.close()

