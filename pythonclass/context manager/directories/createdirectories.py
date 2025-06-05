import os
new_directory="new_dir.txt"
try:
   os.mkdir(new_directory)
   print(f"{new_directory} is created")
except OSError as e:
    print(f"Error: Failed to create directory '{new_directory}'. {e}")

import os
new_directory="pratyush_directory.txt"
try:
    os.mkdir(new_directory)
    print(f"{new_directory} is created successfully")
except OSError as file: 
    print(f"Error: failed to create dictionary '{new_directory}'.{file}")