class library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self,books):
        self.books.append(books)
    def book_list(self):
        for book in self.books:
            print(f"{book.book_name} by {book.author_name}")

class books:
    def __init__(self,book_name,author_name):
        self.book_name = book_name
        self.author_name = author_name

book1 = books("Atomic Habits", "James cleare")
book2 = books("Harry potter", "J K Rowling")
book3 = books("whatsup people", "unknown man")
Library = library("Sapna Book House")
Library.add_book(book1)
Library.add_book(book2)
Library.add_book(book3)

print(Library.name)
Library.book_list()