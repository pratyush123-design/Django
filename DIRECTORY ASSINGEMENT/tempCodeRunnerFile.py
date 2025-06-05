
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
