def read_book(path):
    with open(path) as f:
        return f.read()
    
def count_words(book_text):
    words = book_text.split()
    number = 0
    for word in words:
        number += 1
    return number

def main():
    book = "books/frankenstein.txt"
    text = read_book(book)
    count = count_words(text)
    print(count)

main()