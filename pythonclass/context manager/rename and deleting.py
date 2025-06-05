# rename
import os
current_name="ram.txt"
new_name="old.txt"
os.rename(current_name,new_name)
print(f"File {current_name} is changed to {new_name}")

#delete
import os
file_to_delete="khatiwada.txt"
os.remove(file_to_delete)
print(f"file {file_to_delete} is deleted successfully")