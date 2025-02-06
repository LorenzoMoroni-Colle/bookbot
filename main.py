def main():
    book = "books/frankenstein.txt"
    text = read_book(book)
    count = count_words(text)
    characters = count_characters(text)
    list = convert_dict(characters)
    list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book} ---")
    print(f"{count} words found in the document")
    print ("")
    for element in list:
        if element["letter"].isalpha():
            print(f"The '{element["letter"]}' character was found {element["num"]} times")
    print("--- End report ---")


def read_book(path):
    with open(path) as f:
        return f.read()
    
def count_words(book_text):
    words = book_text.split()
    number = 0
    for word in words:
        number += 1
    return number

def count_characters(book_text):
    lowered_string = book_text.lower()
    characters = dict()
    for char in lowered_string:
        characters[char] = characters.get(char,0) + 1
    return characters

def convert_dict(dict):
    converted = []
    for key in dict:
        converted.append({"letter":key,"num":dict[key]})
    return converted


def sort_on(dict_of_dict):
    return dict_of_dict["num"]


main()