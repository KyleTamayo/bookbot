import sys
import os

def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content

def main() -> int:
    file_path = os.path.join('books', 'frankenstein.txt')

    print(read_file(file_path))
    
    return 0

if __name__ == '__main__':
    sys.exit(main())