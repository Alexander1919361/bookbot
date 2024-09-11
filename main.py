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
    selection = input("Which book would you like to read? ")
    try:
        if book_list[selection]:
            book = f"{book_list[selection]}.txt"
    except KeyError:
        print("Invalid selection")
        return None
    with open(f"books/{book}", "r") as f:
        return f.read()


def main():
    book_list = get_book_list()
    book_content = open_book(book_list)
    if book_content is not None:
        print(book_content)
    else:
        print("ERROR! ERROR! INVALID SELECTION. FORMATTING HARD DRIVE TO REMOVE POTENTIAL SECURITY THREATS")
        quit()


main()
    