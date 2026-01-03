from stats import count_words

def get_book_text(path_to_file):
    with open(path_to_file, encoding='utf-8') as file:
        contents = file.read()
    return contents

def main():
    filepath = './books/frankenstein.txt'
    book_contents = get_book_text(filepath)
    #print(book_contents)
    count = count_words(book_contents)
    print(f'Found {count} total words')


if __name__ == "__main__":
    main()
