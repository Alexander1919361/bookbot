import os

def get_book_list():
    book_list = dict()
    counter = 65  # ASCII code for 'A'
    try:
        with open('books/book_list.txt', 'r') as f:     #'r' specifies 'read only'
            for line in f:
                stripped_line = line.strip()
                if stripped_line:  # This will be False for empty strings
                    book_list[chr(counter)] = stripped_line
                    counter += 1
                    if counter > 90:  # ASCII code for 'Z'
                        break
    except FileNotFoundError:
        print("book_list.txt not found.")
    return book_list

def open_book(book_list):
    for key, value in book_list.items():
        print("Book list:")
        print(f"{key}: {value}")
    selection = input("Which book would you like to review? ")
    try:
        if book_list[selection]:
            book = f"{book_list[selection]}.txt"
    except KeyError:
        print("Invalid selection")
        return None
    with open(f"books/{book}", "r") as f:
        return f.read()
    
def wordcount(book_content):
    word_list = book_content.split()
    return len(word_list)

def charactercount(book_content):
    characters = dict()
    for character in book_content.lower():
        if character != "\n":
            if character not in characters:
                characters[character] = 1
            else:
                characters[character] += 1
    return sorted(characters.items())

def characters_list(characters_dict):
    charlist = []
    for character, count in characters_dict:
        if character.isalpha():
            charlist.append({"character": character, "count": count})
    return charlist

def main():
    print("Book analysis project.")
    print("This program will analyse a book .txt file located in /books, and provide a word count and alphabet character count.\nBooks must be added to the book_index.txt")
    book_list = get_book_list()
    book_content = open_book(book_list)
    if book_content is not None:
        #print(book_content)
        print(f"Word count: {wordcount(book_content)}")
        characters_dict = charactercount(book_content)
        charlist = characters_list(characters_dict)
        charlist.sort(key=lambda x: x["count"], reverse=True)
        for char_dict in charlist:
            print(f"The '{char_dict['character']}' character was found {char_dict['count']} times! Wow!")
        print("End of report.")
        
    else:
        print("ERROR! ERROR! INVALID SELECTION. FORMATTING HARD DRIVE TO REMOVE POTENTIAL SECURITY THREATS")
        quit()



main()
    