def find_book(self, book_id):
    for book in self.books:
        if book.book_id == book_id:
            return book

    return None


def find_member(self, member_id):
    for member in self.members:
        if member.member_id == member_id:
            return member

    return None


def search_book(self, keyword):
    for book in self.books:

        if keyword.lower() in book.title.lower() \
                or keyword.lower() in book.author.lower():
            book.display_info()
