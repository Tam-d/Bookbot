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