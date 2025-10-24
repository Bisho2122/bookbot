import sys
from stats import count_words, count_chars, sort_dict

if not len(sys.argv) == 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(sys.argv[1])
    n_words = count_words(book_text)
    chars_dict = count_chars(book_text)
    sorted_list = sort_dict(chars_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {n_words} total words")
    print("--------- Character Count -------")
    for char_stat in sorted_list:
        char = char_stat['char']
        num = char_stat['num']
        if char_stat['char'].isalpha():
            print(f"{char}: {num}")
        else:
            continue
    print("============= END ===============")

main()