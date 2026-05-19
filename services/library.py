from config import BOOKS_CSV, MEMBERS_CSV
from models.book import Book
from models.member import Member
from utils.util import add_record, delete_record, clear_csv, process_book_transaction


def add_book():
    book_title = input("Enter Book Name: ")
    book_author = input("Enter Book Author: ")
    book_genre = input("Enter Book Genre: ")
    book = Book(None, book_title, book_author, book_genre)
    add_record(BOOKS_CSV, "Book_ID", "Title", book_title, book, "Book")


def add_member():
    name = input("Enter Member Name: ")
    age = int(input(f"Enter {name} Age: "))
    contact_info = input(f"Enter {name} Contact Info: ")
    member = Member(None, name, age, contact_info)
    add_record(MEMBERS_CSV, "Member_ID", "Name", name, member, "Member")


def delete_book():
    book_title = input("Enter Book Name to be deleted: ")
    delete_record(BOOKS_CSV, "Title", book_title, "Book")


def delete_member():
    member_name = input("Enter Member Name to be deleted: ")
    delete_record(MEMBERS_CSV, "Name", member_name, "Member")


def clear_library_data():
    clear_csv(BOOKS_CSV)
    clear_csv(MEMBERS_CSV)
    print("\nAll library data cleared successfully !")


def issue_book():
    process_book_transaction(
        expected_availability=True,
        updated_availability=False,
        success_message="issued"
    )


def return_book():
    process_book_transaction(
        expected_availability=False,
        updated_availability=True,
        success_message="returned"
    )
