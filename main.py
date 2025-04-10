from stats import word_count, get_book_text
def main():
    contents = get_book_text("books/frankenstein.txt")
    print(word_count(contents))

main()
