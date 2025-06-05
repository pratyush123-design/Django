# import os

# # 1. Make a directory
# def create_directory():
#     dir_name = input("Enter the directory name to create: ")
#     try:
#         os.makedirs(dir_name, exist_ok=True)
#         print(f"Directory '{dir_name}' created.")
#         return dir_name
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

# # 2. Make a file inside that directory
# def create_file(directory):
#     file_name = input("Enter the file name to create inside the directory: ")
#     file_path = os.path.join(directory, file_name)
#     try:
#         with open(file_path, 'w') as f:
#             pass
#         print(f"File '{file_path}' created.")
#         return file_path
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

# # 3. Write some text
# def write_text(file_path):
#     text = input("Enter the text to write: ")
#     try:
#         with open(file_path, 'a') as f:
#             f.write(text + '\n')
#         print("Text written successfully.")
#     except Exception as e:
#         print(f"Error: {e}")

# # 4. Read the file
# def read_file(file_path):
#     try:
#         with open(file_path, 'r') as f:
#             content = f.read()
#         print("File contents:\n", content)
#     except Exception as e:
#         print(f"Error: {e}")

# # 5. Update text without overwriting
# def update_text(file_path):
#     text = input("Enter text to append to the file: ")
#     try:
#         with open(file_path, 'a') as f:
#             f.write(text + '\n')
#         print("Text appended successfully.")
#     except Exception as e:
#         print(f"Error: {e}")

# # 6. Get current working directory and file path
# def get_paths(file_path):
#     try:
#         cwd = os.getcwd()
#         print(f"Current Working Directory: {cwd}")
#         print(f"File Path: {file_path}")
#     except Exception as e:
#         print(f"Error: {e}")

# # 7. Get name and size of the file
# def file_info(file_path):
#     try:
#         size = os.path.getsize(file_path)
#         name = os.path.basename(file_path)
#         print(f"File Name: {name}")
#         print(f"File Size: {size} bytes")
#     except Exception as e:
#         print(f"Error: {e}")

# # 8. Get extension of file
# def file_extension(file_path):
#     try:
#         _, ext = os.path.splitext(file_path)
#         print(f"File Extension: {ext}")
#     except Exception as e:
#         print(f"Error: {e}")

# # 9. Delete the file
# def delete_file(file_path):
#     try:
#         os.remove(file_path)
#         print(f"File '{file_path}' deleted.")
#         return None
#     except Exception as e:
#         print(f"Error: {e}")
#         return file_path

# # Main function with loop
# def main():
#     directory = None
#     file_path = None

#     while True:
#         print("\n--- Choose an action ---")
#         print("1. Create directory")
#         print("2. Create file in directory")
#         print("3. Write text")
#         print("4. Read file")
#         print("5. Append text to file")
#         print("6. Get current directory and file path")
#         print("7. Get file name and size")
#         print("8. Get file extension")
#         print("9. Delete file")
#         print("0. Exit")
        
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             directory = create_directory()

#         elif choice == '2':
#             if directory:
#                 file_path = create_file(directory)
#             else:
#                 print("Please create a directory first.")

#         elif choice == '3':
#             if file_path:
#                 write_text(file_path)
#             else:
#                 print("Please create a file first.")

#         elif choice == '4':
#             if file_path:
#                 read_file(file_path)
#             else:
#                 print("Please create a file first.")

#         elif choice == '5':
#             if file_path:
#                 update_text(file_path)
#             else:
#                 print("Please create a file first.")

#         elif choice == '6':
#             if file_path:
#                 get_paths(file_path)
#             else:
#                 print("Please create a file first.")

#         elif choice == '7':
#             if file_path:
# #                 file_info(file_path)
# #             else:
# #                 print("Please create a file first.")

# #         elif choice == '8':
# #             if file_path:
# #                 file_extension(file_path)
# #             else:
# #                 print("Please create a file first.")

# #         elif choice == '9':
# #             if file_path:
# #                 file_path = delete_file(file_path)
# #             else:
# #                 print("No file to delete.")

# #         elif choice == '0':
# #             print("Exiting the program.")
# #             break

# #         else:
# #             print("Invalid choice. Please enter a number from 0 to 9.")

# # # Run the main function
# # if __name__ == "__main__":
# #     main()

# import os
# #create a directory
# def create_directory():
#     new_directory=input("Enter the name of new directory: ")
#     try:
#         os.mkdir(new_directory)
#         print(f"{new_directory} is created successfully")
#     except OSError as e:
#         print(f"Error {new_directory} not createe as {e}")
# #2. making a file
# def make_file(directory):
#     new_file=input("Enter the name of file: ")
#     made_file=os.path.join(directory,new_file)
#     try:
#         with open(made_file) as f:
#          print(f"{made_file} is created ")
#     except OSError as e:
#         print(f"Error {e}")
# #3 adding text
# def add_text(made_file):
#     text=input("Enter the text you want to add:")
#     try:
#         with open(made_file,'a') as f:
#             f.write(text)
#         print("Text added successfully.")
#     except OSError as e:
#         print(f"Error: {e}")
# # 4 reading TEXT
# def read_file(made_file):
#     try :
#         with open (made_file,'r') as f:
#             sentences=f.read
#         print("File senteces are ", sentences)
#     except OSError as e:
#         print("Error: {e}")
# #5 updating text
# def update_text(made_file):
#     adding_sentences=input("Enter the adding sentences: ")
#     try:
#         with open(made_file,'a') as f:
#             f.append(adding_sentences)
#         print("text appended successfully")
#     except OSError as e:
#         print(f"Error: {e}")
# #6 gettingg current directory
# def get_current_position(made_file):
#     try:
#         position=os.getcwd()
#         print("Current postion is {position} " )
#         print("File path is:{made_File}" )
#     except OSError as e:
#         print("Error: {e}")
    
# #7. getting name an size of the file
# def file_info(made_file):
#     try:
#         intro=os.path.basename(made_file)
#         size=os.path.getsize(made_file)
#         print("Name of file is {intro}")
#         print("Size of file is {size}")
#     except OSError as e:
#         print(f"Error : {e}")

# #8. getting extensions of the file
# def extension(made_file):
#     try:
#         ext=os.path.splitext(made_file)
#         print("The extension of the file is {ext}")
#     except OSError as e:
#         print("Error : {e}")
# #9 Deleting the file
# def delete_file(made_file):
#     try:
#         os.remove(made_file)
#         print("file {made_file} is deleted")
#     except OSError as e:
#         print(f"Error: {e}")
# # Main function with loop
# def main():
#     directory = None
#     file_path = None
#     while True:
#         print("\n Chosse an action ")
#         print("1. create directory ")
#         print("2. Chosse a file in directory ")
#         print("3. adding text ")
#         print("4. reading file ")
#         print("5. appending text to file ")
#         print("6. current working directory and made file ")
#         print("7. getting name and size ")
#         print("8. getting extensions ")
#         print("9. deleting the file. ")

#         choice=input("Enter the number you want to choose: ")
#         if choice=='1':
#             directory=create_directory()
#         elif choice=='2':
#             if directory:
#                 made_file=make_file(directory)
#             else:
#                 print("creaate a dictionary first.")
#         elif choice=='3':
#             if made_file:
#                 add_text(made_file)
#             else:
#                 print("create a file.")
#         elif choice=='4':
#             if made_file:
#               read_file(made_file)
#             else:
#                 print("add text")
#         elif choice=='5':
#             if made_file:
#               update_text(made_file)
#             else:
#                 print('add text to append.')
#         elif choice=='6':
#             if made_file:
#                 get_current_position(made_file)
#             else:
#                 print("please create a file first.")
#         elif choice=='7':
#             if made_file:
#                 file_info(made_file)
#             else:
#                 print("Create file")
#         elif choice=='8':
#             if made_file:
#                 extension(made_file)
#             else:
#                 print("create file")
#         elif choice=='9':
#             if made_file:
#                 delete_file(made_file)
#             else:
#                 print("create file")
#         elif choice=='0':
#             print("exiting the program")
#         else:
#             print("Invalid choice, enter number between 0 to 9")
# if __name__ == "__main__":
#  main()

         


            
   
import os
#create a directory
def create_directory():
    new_directory=input("Enter the name of new directory: ")
    try:
        os.mkdir(new_directory)
        print(f"{new_directory} is created successfully")
    except OSError as e:
        print(f"Error {new_directory} not createe as {e}")
#2. making a file
def make_file(directory):
    new_file=input("Enter the name of file: ")
    made_file=os.path.join(directory,new_file)
    try:
        with open(made_file) as f:
         print(f"{made_file} is created ")
    except OSError as e:
        print(f"Error {e}")
#3 adding text
def add_text(made_file):
    text=input("Enter the text you want to add:")
    try:
        with open(made_file,'a') as f:
            f.write(text)
        print("Text added successfully.")
    except OSError as e:
        print(f"Error: {e}")
# 4 reading TEXT
def read_file(made_file):
    try :
        with open (made_file,'r') as f:
            sentences=f.read
        print("File senteces are ", sentences)
    except OSError as e:
        print("Error: {e}")
#5 updating text
def update_text(made_file):
    adding_sentences=input("Enter the adding sentences: ")
    try:
        with open(made_file,'a') as f:
            f.append(adding_sentences)
        print("text appended successfully")
    except OSError as e:
        print(f"Error: {e}")
#6 gettingg current directory
def get_current_position(made_file):
    try:
        position=os.getcwd()
        print("Current postion is {position} " )
        print("File path is:{made_File}" )
    except OSError as e:
        print("Error: {e}")
    
#7. getting name an size of the file
def file_info(made_file):
    try:
        intro=os.path.basename(made_file)
        size=os.path.getsize(made_file)
        print("Name of file is {intro}")
        print("Size of file is {size}")
    except OSError as e:
        print(f"Error : {e}")

#8. getting extensions of the file
def extension(made_file):
    try:
        ext=os.path.splitext(made_file)
        print("The extension of the file is {ext}")
    except OSError as e:
        print("Error : {e}")
#9 Deleting the file
def delete_file(made_file):
    try:
        os.remove(made_file)
        print("file {made_file} is deleted")
    except OSError as e:
        print(f"Error: {e}")
# Main function with loop
def main():
    directory = None
    file_path = None
    while True:
        print("\n Chosse an action ")
        print("1. create directory ")
        print("2. Chosse a file in directory ")
        print("3. adding text ")
        print("4. reading file ")
        print("5. appending text to file ")
        print("6. current working directory and made file ")
        print("7. getting name and size ")
        print("8. getting extensions ")
        print("9. deleting the file. ")

        choice=input("Enter the number you want to choose: ")
        if choice=='1':
            directory=create_directory()
        elif choice=='2':
            if directory:
                made_file=make_file(directory)
            else:
                print("creaate a dictionary first.")
        elif choice=='3':
            if made_file:
                add_text(made_file)
            else:
                print("create a file.")
        elif choice=='4':
            if made_file:
              read_file(made_file)
            else:
                print("add text")
        elif choice=='5':
            if made_file:
              update_text(made_file)
            else:
                print('add text to append.')
        elif choice=='6':
            if made_file:
                get_current_position(made_file)
            else:
                print("please create a file first.")
        elif choice=='7':
            if made_file:
                file_info(made_file)
            else:
                print("Create file")
        elif choice=='8':
            if made_file:
                extension(made_file)
            else:
                print("create file")
        elif choice=='9':
            if made_file:
                delete_file(made_file)
            else:
                print("create file")
        elif choice=='0':
            print("exiting the program")
        else:
            print("Invalid choice, enter number between 0 to 9")
if __name__ == "__main__":
 main()



import os

# 1. create a directory
def create_directory():
    new_directory = input("Enter the name of new directory: ")
    try:
        os.mkdir(new_directory)
        print(f"{new_directory} is created successfully")
        return new_directory  # Return directory name
    except OSError as e:
        print(f"Error: {new_directory} not created because {e}")
        return None

# 2. making a file
def make_file(directory):
    new_file = input("Enter the name of file: ")
    made_file = os.path.join(directory, new_file)
    try:
        with open(made_file, 'w') as f:  # Use 'w' mode to create the file
            pass
        print(f"{made_file} is created")
        return made_file  # Return full file path
    except OSError as e:
        print(f"Error: {e}")
        return None

# 3. adding text
def add_text(made_file):
    text = input("Enter the text you want to add: ")
    try:
        with open(made_file, 'a') as f:
            f.write(text)
        print("Text added successfully.")
    except OSError as e:
        print(f"Error: {e}")

# 4. reading text
def read_file(made_file):
    try:
        with open(made_file, 'r') as f:
            sentences = f.read()  # Call read() as a function
        print("File sentences are:\n", sentences)
    except OSError as e:
        print(f"Error: {e}")

# 5. updating text (append more text)
def update_text(made_file):
    adding_sentences = input("Enter the sentences you want to append: ")
    try:
        with open(made_file, 'a') as f:
            f.write(adding_sentences)  # use write(), no append() for file object
        print("Text appended successfully.")
    except OSError as e:
        print(f"Error: {e}")

# 6. getting current directory and file path
def get_current_position(made_file):
    try:
        position = os.getcwd()
        print(f"Current position is: {position}")
        print(f"File path is: {made_file}")
    except OSError as e:
        print(f"Error: {e}")

# 7. getting name and size of the file
def file_info(made_file):
    try:
        intro = os.path.basename(made_file)
        size = os.path.getsize(made_file)
        print(f"Name of file is: {intro}")
        print(f"Size of file is: {size} bytes")
    except OSError as e:
        print(f"Error: {e}")

# 8. getting extension of the file
def extension(made_file):
    try:
        ext = os.path.splitext(made_file)[1]
        print(f"The extension of the file is: {ext}")
    except OSError as e:
        print(f"Error: {e}")

# 9. deleting the file
def delete_file(made_file):
    try:
        os.remove(made_file)
        print(f"File {made_file} is deleted")
    except OSError as e:
        print(f"Error: {e}")

# Main function with loop
def main():
    directory = None
    made_file = None
    while True:
        print("\nChoose an action:")
        print("1. Create directory")
        print("2. Choose a file in directory (create file)")
        print("3. Add text")
        print("4. Read file")
        print("5. Append text to file")
        print("6. Show current working directory and file path")
        print("7. Get file name and size")
        print("8. Get file extension")
        print("9. Delete the file")
        print("0. Exit")

        choice = input("Enter the number you want to choose: ")

        if choice == '1':
            directory = create_directory()
        elif choice == '2':
            if directory:
                made_file = make_file(directory)
            else:
                print("Create a directory first.")
        elif choice == '3':
            if made_file:
                add_text(made_file)
            else:
                print("Create a file first.")
        elif choice == '4':
            if made_file:
                read_file(made_file)
            else:
                print("Create a file first.")
        elif choice == '5':
            if made_file:
                update_text(made_file)
            else:
                print("Create a file first.")
        elif choice == '6':
            if made_file:
                get_current_position(made_file)
            else:
                print("Create a file first.")
        elif choice == '7':
            if made_file:
                file_info(made_file)
            else:
                print("Create a file first.")
        elif choice == '8':
            if made_file:
                extension(made_file)
            else:
                print("Create a file first.")
        elif choice == '9':
            if made_file:
                delete_file(made_file)
                made_file = None  # Reset file after deletion
            else:
                print("Create a file first.")
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, enter number between 0 to 9.")

if __name__ == "__main__":
    main()
