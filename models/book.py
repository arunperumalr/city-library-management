class Book:

    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = True

    def to_dict(self):
        return {
            "Book_ID": self.book_id,
            "Title": self.title,
            "Author": self.author,
            "Genre": self.genre,
            "Availability": self.is_available
        }