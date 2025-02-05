file_path = "/home/drea/Bookbot/books/frankenstein.txt"

# Open the file and read its contents
with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
