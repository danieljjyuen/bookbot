def main():
    path = 'books/frankenstein.txt'
    file_content = read_file(path)
    print(file_content)
    print(f"word count is {word_count(file_content)}")
    character_dict = character_count(file_content)
    print(character_dict)
    print_report(character_dict)

def read_file(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def character_count(text):
    dict = {}
    text = text.lower()
    for char in text:
        if char in dict:
            dict[char] = dict[char]+1
        else:
            dict[char] = 1
    return dict

def sort_on(dict):
    return dict[1]

def print_report(dict):
    dict_sorted = sorted(dict.items(), reverse=True, key=sort_on)
    for entry in dict_sorted:
        if entry[0].isalpha():
            print(f"The {entry[0]} character was found {entry[1]} times")
        
main()