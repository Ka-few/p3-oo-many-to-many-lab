# many_to_many.py

class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        """Return all contracts for this author."""
        return [c for c in Contract.all if c.author == self]

    def books(self):
        """Return all books for this author."""
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new contract for this author."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the sum of all royalties for this author."""
        return sum(c.royalties for c in self.contracts())


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        """Return all contracts for this book."""
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        """Return all authors for this book."""
        return [c.author for c in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts matching the given date."""
        return [c for c in cls.all if c.date == date]
