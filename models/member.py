class Member:

    def __init__(self, member_id, name, age, contact):
        self.member_id = member_id
        self.name = name
        self.age = age
        self.contact = contact
        self.borrowed_books = []

    def to_dict(self):
        return {
            "Member_ID": self.member_id,
            "Name": self.name,
            "Age": self.age,
            "Contact_Info": self.contact,
            "Borrowed_Books": self.borrowed_books
        }