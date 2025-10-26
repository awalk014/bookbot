from stats import count_words
from stats import count_letters
from stats import letter_sort
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    word_count = count_words(get_book_text(sys.argv[1]))
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    letter_count = letter_sort(count_letters(get_book_text(sys.argv[1])))
    for item in letter_count:
        print(f"{item["name"]}: {item["num"]}")
    print("============= END ===============")

    

main()