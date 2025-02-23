import sys
from stats import getBookText, getWordCount, getCharCount, sortChars 

def main():
    # Check whether the correct number of arguments is passed
    # If not, provide usage instructions and exit the program with an error status
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Store the book's file path provided through the command line argument
    book_path = sys.argv[1]
    
    # Read the entire text of the book from the given file path
    text = getBookText(book_path)
    
    # Calculate the total word count in the book's text
    word_count = getWordCount(text)
    
    # Get the count of each character appearing in the text
    char_count = getCharCount(text)

    # Sort the character counts for cleaner output (likely by frequency or alphabetically)
    sorted_chars = sortChars(char_count)
    
    # Print a formatted report to the console
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Iterate through the sorted character counts and print them to the console
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['count']}")
    
    # Conclude the report
    print("============= END ===============")

main()

