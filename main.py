def main():
    file_path = "../BookBot/books/frankenstein.txt"
    file_content = file_to_read(file_path)
    length , words = count_words(file_content)
    
    char_counter = count_ch_in_book(file_content)
    char_counter = dict(sorted(char_counter.items(),key= lambda item: item[1], reverse=True))
    
    #print report
    print_report(char_counter, length)
    

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

def print_report(ans, total_words):
    only_alphas = {}
    for i in ans:
        if i.isalpha():
            only_alphas[i] = ans[i]
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document \n")
    
    for i in only_alphas:
        print(f"The '{i}' character was found {only_alphas[i]} times")
    print("--- End report ---")
    
main()
