def get_book_word_count(book_text):
    return len(book_text.split())

def get_book_char_count(book_text):

    char_dictionary = {}

    for c in book_text:

        curr_character = c.lower()

        if curr_character in char_dictionary:
            char_dictionary[curr_character] += 1
        else:
            char_dictionary[curr_character] = 1
    
    return char_dictionary