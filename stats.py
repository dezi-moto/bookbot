from operator import itemgetter
def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_char(text: str) -> int:
    char_count = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char == '\ufeff':
            continue
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
    return char_count

def sort_on(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=itemgetter('num'), reverse=True)
    return sorted_list