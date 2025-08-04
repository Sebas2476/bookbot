#this will keep our function that is used to count the total num of words in our book
def num_of_words(result):
    num_words = 0
    splits = result.split()
    for split in splits:
        num_words += 1
    return f"{num_words} words found in the document"




