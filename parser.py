import sys
import os

#file opener and reading function
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
 #           print(file.read())
 #           file.seek(0)
            lines = []
            for line in file:
                lines.append(line.strip())
            
    except:
        pass

    return lines #returning list-output

if __name__ == "__main__":
    print(read_file())
