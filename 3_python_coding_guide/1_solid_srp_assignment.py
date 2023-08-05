# Implement a simple program to interact with
# the library catalog system. Create a Python class Book to represent a single book with
# attributes: Title, Author, ISBN, Genre, Availability (whether the book is available for
# borrowing or not). Create another Python class LibraryCatalog to manage the
# collection of books with following functionalities:
# - Add books by storing each book objects (Hint: Create an empty list in constructor
# and store book objects)
# - get book details and get all books from the list of objects
# Lets say, we need a book borrowing process (what books are borrowed and what books
# are available for borrowing). Implement logics to integrate this requirement in the above
# system. Design the classes with a clear focus on adhering to the Single Responsibility
# Principle(SRP) which represents that "A module should be responsible to one, and
# only one, actor."


class Book:
    def __init__(self, title, author, ISBN, genre, availability):
        self._title = title
        self._author = author
        self._ISBN = ISBN
        self._genre = genre
        self._availability = availability

    def get_book_details(self):
        return f'Title: {self._title}\nAuthor: {self._author}\nISBN: {self._ISBN}\nGenre: {self._genre}\nAvailability: {self._availability}\n'


class LibraryCatalog:
    def __init__(self):
        self._book_list = []
    
    def store_book(self, book):
        self._book_list.append(book)
        print("Book stored")

    def get_all_books(self):
        return self._book_list


class BorrowBook:
    def __init__(self):
        self._borrowed_books = []
    
    def borrow_book(self, book):
        self._borrowed_books.append(book)
        print("Book borrowed")
    
    def get_borrowed_books(self):
        return self._borrowed_books


if __name__ == "__main__":
    b1 = Book("Programming", "RajKumar", 111, 'Course', True)
    b2 = Book("Python", "RajKumarBiswokarma", 112, 'Course', True)

    lib = LibraryCatalog()
    lib.store_book(b1)
    lib.store_book(b2)

    all_books = lib.get_all_books()

    # Getting all books in the library
    print("All Books in the Library:")
    for book in all_books:
        print(book.get_book_details())

    borrow = BorrowBook()
    borrow.borrow_book(b1)
    borrow.borrow_book(b2)

    # All borrowed books
    all_borrowed_books = borrow.get_borrowed_books()
    print("\nAll Borrowed Books:")
    for book in all_borrowed_books:
        print(book.get_book_details())
