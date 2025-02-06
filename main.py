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

def main():
    book = "books/frankenstein.txt"
    text = read_book(book)
    count = count_words(text)
    characters = count_characters(text)
    print(characters)

main()