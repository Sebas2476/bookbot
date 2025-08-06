#this will keep our function that is used to count the total num of words in our book
def num_of_words(result):
    num_words = 0
    splits = result.split()
    for split in splits:
        num_words += 1
    
    message = f"Found {num_words} total words"
    return message


def num_of_chars(book_for_dict):
    symbol_dict = {}
    words = book_for_dict.lower()
    for charr in words:
        if charr not in symbol_dict:
            symbol_dict[charr] = 1
        else:
            symbol_dict[charr] += 1
    return symbol_dict

def sort_func(input_for_dict): 
    sort_list = []
    dicts = num_of_chars(input_for_dict)
    for key, value in dicts.items():
        if key.isalpha():
            sort_list.append({"char": key, "num": value})
    sort_list.sort(reverse=True, key=lambda item: item["num"] )
    return sort_list


