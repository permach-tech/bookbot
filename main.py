import sys
from stats import get_num_words, get_num_characters, sorted_book_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return str(file_contents)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_arg}...")
    text = get_book_text(book_arg)
    count = get_num_words(text)
    char_counts = get_num_characters(text)
    sorted_chars = sorted_book_list(char_counts)
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char, num in sorted_chars:
        print(f"{char}: {num}")
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_arg = sys.argv[1]
    main()