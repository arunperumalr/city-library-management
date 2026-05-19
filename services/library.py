class Library:

    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    # def add_book(self, book):
    #     self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_member(self, member_id):

        for member in self.members:
            if member.member_id == member_id:
                return member

        return None

    def find_book(self, book_id):

        for book in self.books:
            if book.book_id == book_id:
                return book

        return None

    def issue_book(self, member_id, book_id):

        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print("Member not found")
            return

        if not book:
            print("Book not found")
            return

        if not book.is_available:
            print("Book already issued")
            return

        book.issue_book()
        member.borrow_book(book)

        print("Book issued successfully")

    # ADD THIS METHOD
    def search_book(self, keyword):

        found = False

        for book in self.books:

            if keyword.lower() in book.title.lower() \
                    or keyword.lower() in book.author.lower():
                print(f"""
Book ID   : {book.book_id}
Title     : {book.title}
Author    : {book.author}
Genre     : {book.genre}
Available : {book.is_available}
""")

                found = True

        if not found:
            print("No books found")


