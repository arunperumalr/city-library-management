from datetime import datetime

class BorrowTransaction:

    def __init__(self, member_id, book_id, action):
        self.member_id = member_id
        self.book_id = book_id
        self.action = action
        self.date = datetime.now()