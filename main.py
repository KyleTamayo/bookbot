import sys
import os

def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content

def num_words(file_path) -> int:
    content = read_file(file_path)
    count = 0

    content = content.split()
    for word in content:
        count += 1
    
    return count

def character_count(file_path) -> dict:
    content = read_file(file_path)
    char_count = {}

    for c in content.lower():
        char_count[c] = char_count[c] + 1 if c in char_count else 1

    return(char_count)

def main() -> int:
    file_path = os.path.join('books', 'frankenstein.txt')

    print(f"Number of words: {num_words(file_path)}")
    print(character_count(file_path))
    
    return 0

if __name__ == '__main__':
    sys.exit(main())