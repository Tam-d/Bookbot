from stats import get_book_word_count, get_book_char_count, sort_char_dictionary
from report import print_report


def get_book_text(file_path):

    file_contents = ""

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    book_word_count = get_book_word_count(book_text)
    book_char_count = get_book_char_count(book_text)
    sorted_chars = sort_char_dictionary(book_char_count)

    print_report(book_word_count, sorted_chars)

main()