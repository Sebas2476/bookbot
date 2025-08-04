from stats import num_of_words
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    book = get_book_text("books/frankenstein.txt")
    print(book)
    result = num_of_words(book)
    print(result)

main()