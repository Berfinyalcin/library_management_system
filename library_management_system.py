class Library():
    def __init__(self): # Open the books.txt file and assign it to the class property self.file.
        self.file = open("books.txt", "a+")

    def list_books(self): # To list all the books in the library
        self.file.seek(0)  # Return to the beginning of the file
        books = self.file.readlines() # Return all lines of the file as a list
        if not books:
            print("The library is empty.")
        else:
            for book in books:
                book_info = book.strip().split(',')
                book_name = book_info[0]
                author_name = book_info[1]
                release_date = book_info[2]
                num_pages = book_info[3]
                print(f"Book name: {book_name}, Author name: {author_name}, Release date:{release_date}, Number of pages: {num_pages}")

    def add_book(self): # To add a new book
        book_name = input("Enter the book name:")
        author_name = input("Enter the author's name:")
        release_date = input("Enter the release date:")
        num_pages = input("Enter the number of pages:")
        book_entry = f"{book_name},{author_name},{release_date},{num_pages}"
        self.file.write(book_entry)
        print("The book has been added to the list.")

    def remove_book(self): # To remove a book from the library
        book_title = input("Please enter the name of the book you want to delete:")
        self.file.seek(0)  # Return to the beginning of the file
        books = self.file.readlines() # Read all lines from the books.txt file and assign them to a list variable 'books'
        self.file.seek(0)
        self.file.truncate()

        removed = False
        for book in books:
            if book_title not in book:
                self.file.write(book)
            else:
                removed = True

        if removed:
            print(f"'{book_title}' named book has been removed from the library.")
        else:
            print(f"'{book_title}' named book could not be found in the library.")

    def __del__(self): #When the Library object is destroyed (e.g., when the program ends), this method is automatically called. It closes the file associated with the object.
        self.file.close()

library = Library()

print("""
Welcome to the Library Management System.
1. List books
2. Add book
3. Remove book
Press Q to exit.
""")

while True:
    operation = input("Operation:")
    if operation.lower() == "q":
        print("Exiting...")
        break
    elif operation == "1":
        library.list_books()
    elif operation == "2":
        library.add_book()
    elif operation == "3":
        library.remove_book()
    else:
        print("Invalid operation. Please try again.")
