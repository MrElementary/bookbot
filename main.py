def main():
    book_path = "books/frankenstein.txt"
    text = open_book_path(book_path)
    num_words = get_num_words(text)
    char_dict = count_char(text)
    
    print(f"""--- Begin report of books/frankenstein.txt ---
{num_words} words found in the document\n""")
    for i in char_dict:
        print(f"The '{i}' character was found {char_dict[i]} times")
    print("--- End report---")


def open_book_path(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def count_char(text):
    my_dict = {}
    text = text.lower()
    for i in text:
        if i in my_dict:
            my_dict[i] += 1
        else:
            if i.isalpha():
                my_dict[i] = 1
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


if __name__ == '__main__':
    main()
