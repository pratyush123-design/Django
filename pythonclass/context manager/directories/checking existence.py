import os 
directory_path="pratyush_directory.txt"
if os.path.exists(directory_path):
    print(f"the directory {directory_path} exists")
else:
    print(f"the directory {directory_path} does not exists")


import os 
current_directory=os.getcwd
print(f"curret directry is : {current_directory}" )


import os
directory_path = r"D:\MyFolder\new_dir"

try:
   os.rmdir(directory_path)
   print(f"Directory '{directory_path}' successfully removed.")
except OSError as e:
   print(f"Error: Failed to remove directory '{directory_path}'. {e}")