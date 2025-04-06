# (Make a class for a book and a library)
# (Make methods to add a book to a library)
# Make a class for periodicals (magazines) and a parent class for publications (books and periodicals)

from dataclasses import dataclass, field


@dataclass
class Publication:
    ...

@dataclass
class Book(Publication):
    ...

@dataclass
class Periodical(Publication):
    ...

@dataclass
class Library:
    ...


if __name__ == "__main__":
    book = Book(
        title="The Catcher in the Rye",
        year=1951,
        publisher="Little, Brown and Company",
        author="J.D. Salinger",
    )
    periodical = Periodical(
        title="The New Yorker",
        year=1951,
        publisher="The New Yorker",
        editor="Harold Ross",
        issue=52,
    )
    library = Library()
    library.add_publication(book)
    library.add_publication(periodical)
    print(library.search_by_title_year("The Catcher in the Rye", 1951))
    print(library.search_by_title_year("The Catcher in the Rye", 1952))
    print(library.search_by_title_year("The Catcher in the Rye"))
    print(library.search_by_title_year("The New Yorker", 1951))
    print(library.search_by_title_year("The New Yorker", 1952))
    print(library.search_by_title_year("The New Yorker"))
