def get_book_text(file_path):

    file_contents = ""

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def get_book_word_count(book_text):
    return len(book_text.split())
    


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    book_word_count = get_book_word_count(book_text)

    print(f"Found {book_word_count} total words")


main()