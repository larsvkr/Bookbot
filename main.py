def get_book_text(url):
    with open(url) as f:
        read_contents = f.read()

    return read_contents

def word_count(text):
    number_of_words = len(text.split())
    return f"{number_of_words} words found in the document"

def main():
    contents = get_book_text("books/frankenstein.txt")
    print(word_count(contents))

main()
