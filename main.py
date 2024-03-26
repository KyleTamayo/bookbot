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
    c_count = {}

    for c in content.lower():
        if c in c_count:
            c_count[c] = c_count[c] + 1
        else:
            c_count[c] = 1

    return(c_count)

def sort_on(dict):
    return dict["num"]

def print_c_count(c_count):
    dict_list = []

    for c in c_count:
        if c.isalpha():
            dict_list.append({"char": c, "num": c_count[c]})

    dict_list.sort(reverse=True, key=sort_on)

    for i in dict_list:
        print(f"The \'{i['char']}\' character was found {i['num']} times.")

def main() -> int:
    file_path = os.path.join('books', 'frankenstein.txt')

    print(f"--- Begin report of {file_path}---\n")
    print(f"Number of words: {num_words(file_path)}\n")
    print_c_count(character_count(file_path))
    
    return 0

if __name__ == '__main__':
    sys.exit(main())