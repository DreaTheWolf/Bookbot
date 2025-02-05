
def main():
    #Variables
    path = "/home/drea/Bookbot/books/frankenstein.txt"
    text = getBookText(path)
    wordsCount = getWordCount(text)
    charCount = getCharCount(text)
    sorted_chars = sortChars(charCount)
    
    #Report print begging
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordsCount} words found in the document\n")
    
    # forloop with f-string for list report print
    for char_dict in sorted_chars:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    
    #End of the report
    print("--- End report ---")

#This function sets path to book from books and reads it
def getBookText(path):
    with open(path) as f:
        return f.read()

#This function counts how many words are in the book
def getWordCount(text):
    words = text.split()
    return len(words)

#This function counts characters in the book
def getCharCount(text):
    characters = {} #make a free dict(ionary)
    for character in text: #for loop in text
        lowered = character.lower() #lower the all the characters!
        if lowered in characters: 
            #if we found new lowered in characters then we add it to dict. plus one
            characters[lowered] = characters[lowered] + 1  
            #else (we already found it) so we just add plus one to count in dictionary       
        else:
            characters[lowered] = 1
    #return dict(ionary)    
    return characters 

#sorting function for sort_chars(char_count): function
def sort_on(dict):
    return dict["count"]

#sorting function for individual characters
def sortChars(char_count):
    chars_list = [] #makes free list
    for char, count in char_count.items(): #forloop for char. and counts. (key and value)
        if char.isalpha():  # only include letters
            chars_list.append({"char": char, "count": count}) #adding chars. and counts to empty list 
    chars_list.sort(reverse=True, key=sort_on) #sorting action
    return chars_list #return sorted character list

main()
