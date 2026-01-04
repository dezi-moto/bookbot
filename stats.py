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