from stats import word_count, get_book_text, char_count, sort_char_count, print_book_report
import sys 
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        url = sys.argv[1]
        contents = get_book_text(url)
        count =(word_count(contents))
        dic = char_count(contents)
        sorted_list = sort_char_count(dic)
        #print(sorted_list)
        print_book_report(url, count, sorted_list)

main()
