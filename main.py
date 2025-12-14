from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    booktext = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(booktext)
    print(f"Found {num_words} total words")

main()

