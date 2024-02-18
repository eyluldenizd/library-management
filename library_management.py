class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        """
        List all the books in the books.txt file.
        """
        self.file.seek(0)
        lines = self.file.read().splitlines()
        if not lines:
            print("No books to display in the list.")
            return
        for line in lines:
            book_info = line.split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        """
        Add a book to the books.txt file.
        """
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        book_release_year = input("Enter book release date (YYYY): ")
        number_of_pages = input("Enter number of pages: ")
        book_info = f"{book_title},{book_author},{book_release_year},{number_of_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        """
         Remove a book from the books.txt file.
        """

        book_title = input('Which book do you want to remove: ')
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        if not book_lines:
            print("No book to display in the list")
        self.file.seek(0)
        self.file.truncate()
        removed = False
        for book in book_lines:
            if book_title not in book:
                self.file.write(book)
            else:
                removed = True
        if removed:
            print("Book removed successfully!")
        else:
            print("The specified book was not found.")


lib = Library()

while True:
    print("\n*** MENU*")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = int(input("Enter your choice(1-4): "))

    if choice == 1:
        lib.list_books()
    elif choice == 2:
        lib.add_book()
    elif choice == 3:
        lib.remove_book()
    elif choice == 4:
        print("Quitting the menu...")
        break
    else:
        print("Invalid choice. Please enter your choice again.")