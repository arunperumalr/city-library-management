import pandas as pd
from datetime import datetime
from config import BOOKS_CSV, MEMBERS_CSV, BORROW_LOG_CSV
from models.log import Log


def record_exists(df, name, column_name):
    return name.lower() in df[column_name].str.strip().str.lower().values

def get_record(df, column_name, name):
    return df[df[column_name].str.strip().str.lower() == name.lower()]


def get_available_records(
        df,
        column_one,
        value_one,
        column_two,
        value_two,
        operation
):

    condition_one = (
        df[column_one]
        .astype(str)
        .str.strip()
        .str.lower() == value_one.lower()
    )

    condition_two = (
        df[column_two]
        .astype(str)
        .str.strip()
        .str.lower() == value_two.lower()
    )

    if operation == "&":
        return df[condition_one & condition_two]

    elif operation == "|":
        return df[condition_one | condition_two]

    else:
        raise ValueError("Invalid operation. Use '&' or '|'.")

def update_borrowed_books(
        members_df,
        column_name,
        member_name,
        book_title,
        availability
):

    member_index = members_df[
        members_df[column_name]
        .str.strip()
        .str.lower() == member_name.lower()
    ].index[0]

    current_books = members_df.loc[member_index, "Borrowed_Books"]

    # Convert borrowed books into list
    if pd.isna(current_books) or current_books.strip() == "":
        borrowed_books = []
    else:
        borrowed_books = [
            book.strip()
            for book in current_books.split(",")
        ]

    # -----------------------------------
    # Issue Book
    # -----------------------------------
    if availability:

        borrowed_books.append(book_title)

    # -----------------------------------
    # Return Book
    # -----------------------------------
    else:

        # Check if member rented this book
        if book_title not in borrowed_books:
            print("\nBook is not rented by this member.")
            return False

        borrowed_books.remove(book_title)

    # Convert list back to string
    updated_books = ", ".join(borrowed_books)

    members_df.loc[member_index, "Borrowed_Books"] = updated_books

    return True

def update_book_availability(books_df, book_row, availability):
    book_index = book_row.index[0]
    books_df.loc[book_index, "Availability"] = availability




def add_record(
        csv_file,
        id_column,
        check_column,
        check_value,
        entity_object,
        entity_name
):

    try:

        # Read CSV
        df = pd.read_csv(csv_file)

        normalized_value = check_value.strip().lower()

        # Check duplicate
        if normalized_value in (
                df[check_column]
                .astype(str)
                .str.strip()
                .str.lower()
                .values
        ):

            print(f"\n{entity_name} already exists!")
            return

        # Generate New ID
        new_id = 1 if df.empty else df[id_column].max() + 1

        # Set generated ID
        setattr(entity_object, id_column.lower(), new_id)

        # Add New Row
        df.loc[len(df)] = entity_object.to_dict()

        # Save CSV
        df.to_csv(csv_file, index=False)

        print(f"\n{entity_name} added successfully!")

    except FileNotFoundError:
        print("CSV file not found.")

    except Exception as e:
        print(f"Error: {e}")

def delete_record(csv_file, column_name, value, entity_name):

    try:
        df = pd.read_csv(csv_file)
        normalized_value = value.strip().lower()

        # ✅ compute once
        mask = df[column_name].astype(str).str.strip().str.lower() == normalized_value
        matched_df = df[mask]

        # ✅ validation uses same result
        can_delete, message = can_delete_record(matched_df, entity_name)

        if not can_delete:
            print(f"\n{message}")
            return

        # delete using same mask
        df = df[~mask]
        df.to_csv(csv_file, index=False)

        print(f"\n{entity_name} deleted successfully!")

    except FileNotFoundError:
        print("CSV file not found.")

    except Exception as e:
        print(f"Error: {e}")



def clear_csv(csv_file):

    try:
        # Read CSV to preserve column structure
        df = pd.read_csv(csv_file)

        # Remove all rows
        df = df.iloc[0:0]

        # Save empty dataframe with headers
        df.to_csv(csv_file, index=False)

        print(f"\nCleared all records from {csv_file}")

    except FileNotFoundError:
        print("CSV file not found.")

    except Exception as e:
        print(f"Error: {e}")


def process_book_transaction(expected_availability, updated_availability, success_message):

    try:
        member_name = input("Enter Member Name: ").strip()
        book_title = input("Enter Book Name: ").strip()

        # Read CSV Files
        members_df = pd.read_csv(MEMBERS_CSV)
        books_df = pd.read_csv(BOOKS_CSV)

        members_df["Borrowed_Books"] = (
            members_df["Borrowed_Books"]
            .fillna("")
            .astype(str)
        )

        # -------------------------------
        # Check if member exists
        # -------------------------------

        member_exists = record_exists(
            members_df,
            member_name,
            "Name"
        )

        if not member_exists:
            print("\nMember does not exist.")
            return

        # -------------------------------
        # Check if book exists
        # -------------------------------

        book_exists = record_exists(
            books_df,
            book_title,
            "Title"
        )

        if not book_exists:
            print("\nBook does not exist.")
            return

        # -------------------------------
        # Get Book Row
        # -------------------------------

        book_row = get_record(books_df,"Title", book_title)

        # -------------------------------
        # Check Availability
        # -------------------------------

        availability = book_row.iloc[0]["Availability"]

        if str(availability).lower() != str(expected_availability).lower():

            if expected_availability:
                print("\nBook is already rented !")
            else:
                print("\nThis book is not rented by any members !")

            return

        # -------------------------------
        # Update Borrowed Books
        # -------------------------------

        if not update_borrowed_books(
                members_df,
                "Name",
                member_name,
                book_title,
                availability
        ):
            return

        # -------------------------------
        # Update Book Availability
        # -------------------------------

        update_book_availability(
            books_df,
            book_row,
            updated_availability
        )

        # -------------------------------
        # Save Changes
        # -------------------------------

        members_df.to_csv(MEMBERS_CSV, index=False)
        books_df.to_csv(BOOKS_CSV, index=False)

        print(f"\nBook {success_message} successfully!")
        return member_name, book_title

    except FileNotFoundError:
        print("CSV file not found.")

    except Exception as e:
        print(f"Error: {e}")

def display_books(books_df, heading):

    print(f"\n{heading}")
    print("-" * 50)

    for _, row in books_df.iterrows():

        print(f"Book ID      : {row['Book_ID']}")
        print(f"Title        : {row['Title']}")
        print(f"Author       : {row['Author']}")
        print(f"Genre        : {row['Genre']}")
        print(f"Availability : {row['Availability']}")
        print("-" * 50)

def display_members(members_df, heading):

    print(f"\n{heading}")
    print("-" * 60)

    for _, row in members_df.iterrows():
        print(f"Member ID      : {row['Member_ID']}")
        print(f"Name           : {row['Name']}")
        print(f"Age            : {row['Age']}")
        print(f"Contact Info   : {row['Contact_Info']}")
        print(f"Borrowed Books : {row['Borrowed_Books']}")
        print("-" * 60)

def update_borrow_log(member_name, book_title, action):
    try:
        # Read CSV
        borrow_log_df = pd.read_csv(BORROW_LOG_CSV)

        # Generate Transaction ID
        transaction_id = (
            1 if borrow_log_df.empty
            else borrow_log_df["Transaction_ID"].max() + 1
        )

        # Current Date
        current_date = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Create Log Object
        log = Log(
            transaction_id,
            member_name,
            book_title,
            action,
            current_date
        )

        # Add New Row
        borrow_log_df.loc[len(borrow_log_df)] = log.to_dict()

        # Save CSV
        borrow_log_df.to_csv(BORROW_LOG_CSV, index=False)

    except FileNotFoundError:
        print("Borrow log CSV file not found.")

    except Exception as e:
        print(f"Error: {e}")


def can_delete_record(matched_df, entity_name):
    if matched_df.empty:
        return False, f"{entity_name} not found."

    row = matched_df.iloc[0]

    if entity_name.lower() == "book":
        if not row["Availability"]:
            return False, "Book cannot be deleted because it is currently issued."
        return True, ""

    if entity_name.lower() == "member":
        borrowed = row["Borrowed_Books"]

        if pd.isna(borrowed):
            return True, ""

        borrowed_str = str(borrowed).strip()
        if borrowed_str in ["", "[]", "none"]:
            return True, ""

        return False, "Member cannot be deleted because they still have borrowed books."

    return True, ""