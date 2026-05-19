import pandas as pd
from config import BOOKS_CSV, MEMBERS_CSV

df = pd.read_csv(BOOKS_CSV)

def record_exists(df, name, column_name):
    return name.lower() in df[column_name].str.strip().str.lower().values


def get_record(df, name, column_name):
    return df[df[column_name].str.strip().str.lower() == name.lower()]

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




def add_record(csv_file, id_column, check_column, check_value, entity_object, entity_name):

    try:
        normalized_value = check_value.strip().lower()

        # Check duplicate
        if normalized_value in df[check_column].str.strip().str.lower().values:
            print(f"\n{entity_name} already exists!")
            return

        # Generate New ID
        new_id = 1 if df.empty else df[id_column].max() + 1
        print(f"\ndf.empty: ", df.empty)
        print("\nNew ID: ", new_id)

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
        # Read Existing CSV
        df = pd.read_csv(csv_file)

        normalized_value = value.strip().lower()

        # Check if record exists
        if normalized_value in df[column_name].str.strip().str.lower().values:

            # Remove matching rows
            df = df[df[column_name].str.strip().str.lower() != normalized_value]

            # Save updated dataframe
            df.to_csv(csv_file, index=False)

            print(f"\n{entity_name} deleted successfully!")

        else:
            print(f"\n{entity_name} not found.")

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


def process_book_transaction(
        expected_availability,
        updated_availability,
        success_message
):

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

        book_row = get_record(
            books_df,
            book_title,
            "Title"
        )

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

    except FileNotFoundError:
        print("CSV file not found.")

    except Exception as e:
        print(f"Error: {e}")
