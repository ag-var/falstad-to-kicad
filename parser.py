import sys
import os

#file opener and reading function --> NOT PARSER; ONLY OPENS
def read_file():

    if len(sys.argv) < 2:
        print("incorrect usage. usage: python circuit_parse.py <filename>")
        sys.exit(1)

    file_name = sys.argv[1]

    if not (os.path.exists(file_name)):
        print(f"Error: the file '{file_name}' does not exist")
        sys.exit(1)

    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except:
        pass

if __name__ == "__main__":
    read_file()
