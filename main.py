from stats import word_count, get_book_text, char_count
def main():
    contents = get_book_text("books/frankenstein.txt")
    print(word_count(contents))
    print(char_count(contents))



main()
