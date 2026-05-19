from services.library import add_book, add_member, delete_book, delete_member, issue_book, return_book, \
    clear_library_data

while True:
    print("\nWelcome to the Citi Library!")
    print("\n0. Exit"
          "\n1. Add book"
          "\n2. Add Member"
          "\n3. Delete Book"
          "\n4. Delete Member"
          "\n5. Issue Book"
          "\n6. Return Book"
          "\n7. Clear Library")

    choice = int(input("Please enter your choice: "))
    if choice == 0:
        print("Thank you for using our application, Bye!")
        break

    if choice == 1:
        add_book()

    elif choice == 2:
        add_member()

    elif choice == 3:
        delete_book()

    elif choice == 4:
        delete_member()

    elif choice == 5:
        issue_book()

    elif choice == 6:
        return_book()

    elif choice == 7:
        clear_library_data()

    else:
        print("Invalid Input. Please enter a valid choice.")
