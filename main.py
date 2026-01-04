from stats import count_words, count_char, sort_on


def get_book_text(path_to_file):
    with open(path_to_file, encoding='utf-8') as file:
        contents = file.read()
    return contents

def main():
    filepath = './books/frankenstein.txt'
    book_contents = get_book_text(filepath)
    count = count_words(book_contents)
    char_count = count_char(book_contents)
    final_format = sort_on(char_count)
    #print(book_contents)
    print(f'============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print(f'----------- Word Count ----------')
    print(f'Found {count} total words')
    print('--------- Character Count -------')
    for item in final_format:
        print(f"{item['char']}: {item['num']}")
    print(f'============= END ===============')


if __name__ == "__main__":
    main()
