import sys
from stats import num_of_words, num_of_chars, sort_func 
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
     if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
     else:
        book_path = sys.argv[1]
        book =  get_book_text(book_path)
        result = num_of_words(book)
        sort_dicts = sort_func(book)
        print("============ BOOKBOT ============")
        print(book)
        print("----------- Word Count ----------")
        print(result)
        print("--------- Character Count -------")
        for sort_dict in sort_dicts:
            print(f"{sort_dict["char"]}: {sort_dict["num"]}")
            
        print("============= END ===============")
    
   
    

main()