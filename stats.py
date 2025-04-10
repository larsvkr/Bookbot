def get_book_text(url):
    with open(url) as f:
        read_contents = f.read()
    return read_contents

def word_count(text):
    number_of_words = len(text.split())
    return f"{number_of_words} words found in the document"

def char_count(text):
    amount = {}
    text = text.lower()
    for char in text:
        if char in amount.keys():
            amount[char] += 1 
        else:
            amount[char] = 1
    return amount
        


