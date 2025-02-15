def main():
    with open("books/frankenstein.txt") as f:
        print(f"--- Begin report of {f.name} ---")
        file_contents = f.read()
        num_words = count_words(file_contents)
        print(f"{num_words} words found in the document\n")
        char_dict = count_chrs(file_contents)
        for char, freq in char_dict.items():
            print(f"The '{char}' character was found {freq} times")


def count_words(text):
    num_words = len(text.split())
    return num_words


def count_chrs(text):
    dict = {}
    for char in text:
        if not char.isalpha():
            continue
        if char.lower() in dict:
            dict[char.lower()] += 1
        else:
            dict[char.lower()] = 1
    return dict


main()

