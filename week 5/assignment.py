# File Creation
def create_file():
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Hello World")
            file.write("9101112\n")
            file.write("Welcome Home\n")
        print("File 'my_file.txt' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")
    finally:
        print("done")

# File Reading and Display
def read_file():
    try:
        with open('my_file.txt', 'r') as file:
            print("Contents of 'my_file.txt':")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    finally:
        print("done")

# File Appending
def append_to_file():
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
        print("Content appended to 'my_file.txt' successfully.")
    except Exception as e:
        print(f"Error appending to file: {e}")
    finally:
         print("done")


def main():
    create_file()
    read_file()
    append_to_file()
    read_file() 

if __name__ == "__main__":
    main()
