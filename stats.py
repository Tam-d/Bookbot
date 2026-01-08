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

def sort_item(item):
    return item["num"]

def sort_char_dictionary(char_dict):

    char_list = []

    for key in char_dict:

        per_char_dict = {
            "char" : key,
            "num" : char_dict[key]
        }

        char_list.append(per_char_dict)

    char_list.sort(key=sort_item, reverse=True)

    return char_list
    