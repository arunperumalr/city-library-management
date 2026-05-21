import pandas as pd
from config import BOOKS_CSV, MEMBERS_CSV, BORROW_LOG_CSV
from models.book import Book
from models.member import Member
from utils.util import add_record, delete_record, clear_csv, process_book_transaction, get_available_records, \
    display_books, display_members, get_record, update_borrow_log


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
    clear_csv(BORROW_LOG_CSV)
    print("\nAll library data cleared successfully !")


def issue_book():
    result = process_book_transaction(
        expected_availability=True,
        updated_availability=False,
        success_message="issued"
    )
    process_borrow_log(result, "Issued")


def return_book():
    result = process_book_transaction(
        expected_availability=False,
        updated_availability=True,
        success_message="returned"
    )
    process_borrow_log(result, "Returned")


def show_available_books_by_genre():
    try:
        genre = input("Enter Genre: ").strip()
        books_df = pd.read_csv(BOOKS_CSV)

        # Filter books by: Matching genre & Availability == True
        filtered_books = get_available_records(books_df, "Genre", genre, "Availability", "true", "&")

        # Check if books exist
        if filtered_books.empty:
            print(f"\nNo available books found in genre: {genre}")
            return

        # Display Books
        display_books(filtered_books, f"Available Books in Genre '{genre}':")

    except FileNotFoundError:
        print("CSV file not found.")

    except Exception as e:
        print(f"Error: {e}")


def show_members_with_borrowed_books():
    try:
        # Read CSV
        members_df = pd.read_csv(MEMBERS_CSV)

        # Normalize Borrowed_Books column
        members_df["Borrowed_Books"] = (
            members_df["Borrowed_Books"]
            .fillna("")
            .astype(str)
        )

        # Filter members who borrowed books
        borrowed_members = members_df[
            members_df["Borrowed_Books"]
            .str.strip() != ""
            ]

        # Check if any members found
        if borrowed_members.empty:
            print("\nNo members have borrowed books.")
            return

        # Display Members
        display_members(borrowed_members, "Members Who Have Borrowed Books")

    except FileNotFoundError:
        print("CSV file not found.")

    except Exception as e:
        print(f"Error: {e}")


def search_books():
    try:
        search_value = input("Search Book by Title or Author: ").strip().lower()

        # Read CSV
        books_df = pd.read_csv(BOOKS_CSV)

        # Filter matching books
        matched_books = get_available_records(books_df, "Title", search_value,
                                              "Author", search_value, "|")

        # Check if books found
        if matched_books.empty:
            print("\nNo matching books found.")
            return

        # Display Books
        display_books(matched_books, "Matching Books")

    except FileNotFoundError:
        print("CSV file not found.")

    except Exception as e:
        print(f"Error: {e}")


def show_most_popular_genre():
    try:
        # Read CSV
        books_df = pd.read_csv(BOOKS_CSV)

        # Filter only issued books
        issued_books = books_df[books_df["Availability"] == False]

        # Check if any books are issued
        if issued_books.empty:
            print("\nNo books have been issued yet.")
            return

        # Count genres
        genre_counts = (
            issued_books["Genre"]
            .value_counts()
        )

        # Most popular genre
        most_popular_genre = genre_counts.idxmax()

        # Number of issued books
        issue_count = genre_counts.max()

        # Display Result
        print("\nMost Popular Genre")
        print("-" * 30)
        print(f"Genre            : {most_popular_genre}")
        print(f"Books Issued     : {issue_count}")

    except FileNotFoundError:
        print("CSV file not found.")

    except Exception as e:
        print(f"Error: {e}")


def process_borrow_log(result, action):
    if not result:
        return
    member_name, book_title = result
    update_borrow_log(member_name, book_title, action)
