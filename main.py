from services.library import Library
from models.book import Book
from models.member import Member
from utils.util import add_book, delete_book, add_member, delete_member

while True:
    print("\nWelcome to the Citi Library!")
    print("\n0. Exit"
          "\n1. Add book"
          "\n2. Add Member"
          "\n3. Delete Book"
          "\n4. Delete Member")

    choice = int(input("Please enter your choice: "))
    if choice == 0:
        print("Thank you for using our application, Bye!")
        break

    if  choice == 1:
        add_book()

    elif  choice == 2:
        add_member()

    elif  choice == 3:
        delete_book()

    elif  choice == 4:
        delete_member()

    else:
        print("Invalid Input. Please enter a valid choice.")

# library = Library()
#
# book1 = Book(1, "Harry Potter", "Rowling", "Fantasy")
# book2 = Book(2, "Atomic Habits", "James Clear", "Self Help")
#
# member1 = Member(101, "Arun", 36, "9999999999")
#
# library.add_book(book1)
# library.add_book(book2)
#
# library.add_member(member1)
#
# library.issue_book(101, 1)
#
# library.search_book("Rowling")
