import sys
import os
from stats import count_number_of_words
from stats import inventory_all_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return_value = f.read()
    return return_value

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    if not os.path.exists(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)

    name_of_book = sys.argv[1]
    text_to_parse = get_book_text(name_of_book)
    number_of_words = count_number_of_words(text_to_parse)
    character_inventory = inventory_all_characters(text_to_parse)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {name_of_book}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    for entry in character_inventory:
        print(f"{entry}: {character_inventory[entry]}")

main()