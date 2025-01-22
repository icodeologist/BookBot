from re import split


def main():
    file_path = "../BookBot/books/frankenstein.txt"
    file_content = file_to_read(file_path)
    length , words = count_words(file_content)
    
    char_counter = count_ch_in_book(file_content)
    print(char_counter)


def file_to_read(path):
    with open(path) as f:
        file = f.read()
    return file

def count_words(file):
    words = file.split()
    return len(words), words


def count_ch_in_book(string):
    char_counter = {}
    for j in string:
        j = j.lower()
        if j in char_counter:
            char_counter[j] += 1
        else:
            char_counter[j] = 1
    return char_counter











main()
