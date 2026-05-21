class Log:

    def __init__(
            self,
            transaction_id,
            member_name,
            book_title,
            action,
            date
    ):

        self.transaction_id = transaction_id
        self.member_name = member_name
        self.book_title = book_title
        self.action = action
        self.date = date

    def to_dict(self):

        return {
            "Transaction_ID": self.transaction_id,
            "Member_Name": self.member_name,
            "Book_Title": self.book_title,
            "Action": self.action,
            "Date": self.date
        }