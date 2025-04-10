def get_book_text(url):
    with open(url) as f:
        read_contents = f.read()
    return read_contents

def word_count(text):
    number_of_words = len(text.split())
    return number_of_words 

def char_count(text):
    amount = {}
    text = text.lower()
    for char in text:
        if char in amount.keys():
            amount[char] += 1 
        else:
            amount[char] = 1
    return amount


def sort_char_count(chars):
    def sort_on(dic):
        return dic["char"]

    list_chars = []
    for key, val in chars.items():
        num = {}
        num["char"] = key
        num["count"] = val
        list_chars.append(num)
        #print(list_chars)
    list_chars.sort(reverse=True, key=sort_on)
    return list_chars
   
def print_book_report(url, word_count, char_dic):
        print(" ============ BOOKBOT ============")
        print(f"Analyzing book found at {url}")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for row in char_dic:
            if row["char"].isalpha():
                print(f"{row['char']}: {row['count']}")
        print("============= END ===============")
    


