import pandas as pd
from config import BOOKS_CSV, MEMBERS_CSV
from models.book import Book
from models.member import Member

df = pd.read_csv(BOOKS_CSV)

def add_book():
    book_title = input("Enter Book Name: ")
    book_author = input("Enter Book Author: ")
    book_genre = input("Enter Book Genre: ")
    book = Book( None, book_title, book_author, book_genre)
    add_record(BOOKS_CSV,"Book_ID","Title", book_title, book, "Book")

def add_member():
    name = input("Enter Member Name: ")
    age = int(input(f"Enter {name} Age: "))
    contact_info = input(f"Enter {name} Contact Info: ")
    member = Member(None, name, age, contact_info)
    add_record(MEMBERS_CSV,"Member_ID", "Name", name, member,"Member")

def delete_book():
    book_title = input("Enter Book Name to be deleted: ")
    delete_record(BOOKS_CSV,"Title",book_title,"Book" )


def delete_member():
    member_name = input("Enter Member Name to be deleted: ")
    delete_record(MEMBERS_CSV, "Name", member_name, "Member")


def add_record(csv_file, id_column, check_column, check_value, entity_object, entity_name):

    try:
        # Read Existing CSV
        df = pd.read_csv(csv_file)

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