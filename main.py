
def main():
    path = "/home/drea/Bookbot/books/frankenstein.txt"
    text = getBookText(path)
    wordsCount = getWordCount(text)
    charCount = getCharCount(text)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordsCount} words found in the document\n")
    
    # Get your sorted list of characters
    sorted_chars = sort_chars(charCount)
    
    # Print each character count
    for char_dict in sorted_chars:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    
    print("--- End report ---")


def getWordCount(text):
    words = text.split()
    return len(words)

def getCharCount(text):
    characters = {}
    for character in text:
        lowered = character.lower()
        if lowered in characters:
            characters[lowered] = characters[lowered] + 1  
        else:
            characters[lowered] = 1
    return characters

def sort_on(dict):
    return dict["count"]

def sort_chars(char_count):
    chars_list = []
    for char, count in char_count.items():
        if char.isalpha():  # only include letters
            chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list



def getBookText(path):
    with open(path) as f:
        return f.read()


main()
