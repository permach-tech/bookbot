def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    lowered = text.lower()
    char_counts = {}
    for char in lowered:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts


def sorted_book_list(char_counts):
    def sort_key(item):
        return item[0]
    sorted_chars = sorted(char_counts.items(), key=sort_key)
    return sorted_chars
