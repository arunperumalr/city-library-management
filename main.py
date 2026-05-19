from services.library import add_book, add_member, delete_book, delete_member, issue_book, return_book, \
    clear_library_data, show_available_books_by_genre, show_members_with_borrowed_books, search_books, \
    show_most_popular_genre

while True:
    print("\nWelcome to the Citi Library!")
    print("\n0. Exit"
          "\n1. Add book"
          "\n2. Add Member"
          "\n3. Delete Book"
          "\n4. Delete Member"
          "\n5. Issue Book"
          "\n6. Return Book"
          "\n7. Available Books by Genre"
          "\n8. Members who borrowed books"
          "\n9. Search books"
          "\n10. Most Popular Genre"
          "\n11. Clear Library")

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
        show_available_books_by_genre()

    elif choice == 8:
        show_members_with_borrowed_books()

    elif choice == 9:
        search_books()

    elif choice == 10:
        show_most_popular_genre()

    elif choice == 11:
        clear_library_data()

    else:
        print("Invalid Input. Please enter a valid choice.")
