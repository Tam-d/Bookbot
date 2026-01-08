from stats import get_book_word_count, get_book_char_count, sort_char_dictionary


def get_book_text(file_path):

    file_contents = ""

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def print_word_count(word_count):
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")


def print_char_dict(char_dict):
    print(f"{char_dict["char"]}: {char_dict["num"]}")

def print_char_dict_list(char_dict_list):
    for item in char_dict_list:
        print_char_dict(item)

def print_char_count(char_dict_list):
    print("--------- Character Count -------")
    print_char_dict_list(char_dict_list)

def print_report(word_count, char_dict_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print_word_count(word_count)
    print_char_count(char_dict_list)

    print("============= END ===============")

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    book_word_count = get_book_word_count(book_text)
    book_char_count = get_book_char_count(book_text)
    sorted_chars = sort_char_dictionary(book_char_count)

    print_report(book_word_count, sorted_chars)

main()