from stats import count_words, count_chrs
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        print(f"--- Begin report of {f.name} ---")
        file_contents = f.read()
        num_words = count_words(file_contents)
        print(f"{num_words} words found in the document\n")
        char_dict = count_chrs(file_contents)
        for char, freq in char_dict.items():
            print(f"{char}: {freq}")


main()

