try:
    file=open("ram.txt","w")
    file.write("This is an examaple with exception handling")  #if shows error doesnot care
finally:   #it runs finally 
    file.close()
    print("File closed successfully!!")