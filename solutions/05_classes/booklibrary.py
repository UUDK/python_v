# Make a class for a book and a library
# Make methods to add a book to a library

from dataclasses import dataclass, field


@dataclass
class Book:
    title: str
    author: str
    year: int
    publisher: str


@dataclass
class Library:
    books: list[Book] = field(default_factory=list)

    def add_book(self, book: Book):
        self.books.append(book)

    def search_books(self, author: str):
        return [book for book in self.books if book.author == author]


if __name__ == "__main__":
    book1 = Book(
        title="The Catcher in the Rye",
        author="J.D. Salinger",
        year=1951,
        publisher="Little, Brown and Company",
    )
    book2 = Book(
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        year=1925,
        publisher="Charles Scribner's Sons",
    )
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    print(library.search_books("J.D. Salinger"))
    print(library.search_books("F. Scott Fitzgerald"))
    print(library.search_books("Ernest Hemingway"))
    print(library.search_books("J.D. Salinger"))
    print(library.search_books("F. Scott Fitzgerald"))
    print(library.search_books("Ernest Hemingway"))
