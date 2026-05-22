# City Library Management System

The City Library Management System is a console-based Python application developed using Object-Oriented Programming (OOP), Pandas, and CSV file handling. The project simulates a real-world library system where books and members can be managed efficiently through a menu-driven interface.

The application stores data in three CSV files:

* `books_data.csv` → stores book details and availability
* `members_data.csv` → stores member details and borrowed books
* `borrow_log.csv` → stores borrow/return transaction history

## Features

**0. Exit**
Closes the application safely.

**1. Add Book**
Adds a new book into `books_data.csv` with automatic Book ID generation and default availability as `True`.

**2. Add Member**
Adds a new member into `members_data.csv` with automatic Member ID generation.

**3. Delete Book**
Removes a book record from `books_data.csv`.

**4. Delete Member**
Removes a member record from `members_data.csv`.

**5. Issue Book**
Issues a book to a member by updating:

* `books_data.csv` → Availability changed to `False`
* `members_data.csv` → Updates `Borrowed_Books`
* `borrow_log.csv` → Records transaction as “Issued”

**6. Return Book**
Returns a book by updating:

* `books_data.csv` → Availability changed to `True`
* `members_data.csv` → Removes book from `Borrowed_Books`
* `borrow_log.csv` → Records transaction as “Returned”

**7. Available Books by Genre**
Displays all available books filtered by genre from `books_data.csv`.

**8. Members Who Borrowed Books**
Displays members currently having borrowed books from `members_data.csv`.

**9. Search Books**
Searches books by title or author from `books_data.csv`.

**10. Most Popular Genre**
Displays the genre with the highest number of issued books using `books_data.csv`.

**11. Clear Library**
Deletes all records from all CSV files while preserving headers.

---

## Technologies Used

- Python
- Pandas
- CSV File Storage
- Object-Oriented Programming (OOP)

---

## Project Structure

```text
## Project Structure

city-library-management/
│
├── data_base/
│   ├── books_data.csv
│   ├── members_data.csv
│   └── borrow_log.csv
│
├── models/
│   ├── book.py
│   ├── member.py
│   └── log.py
│
├── services/
│   └── library.py
│
├── utils/
│   └── util.py
│
├── config.py
├── main.py
└── README.md
```

---

## How to Run the Project

### 1. Clone Repository

```bash
git clone <repository_url>
```

### 2. Install Dependencies

```bash
pip install pandas
```

### 3. Run Application

```bash
python main.py
```

---

## Menu Options

```text
0. Exit
1. Add Book
2. Add Member
3. Delete Book
4. Delete Member
5. Issue Book
6. Return Book
7. Available Books by Genre
8. Members who Borrowed Books
9. Search Books
10. Most Popular Genre
11. Clear Library
```

---

## Future Improvements

- Support more than one copy of a book
- SQLite/MySQL Database Integration
- GUI using Tkinter or PyQt
- Flask/Django Web Application
- Due Dates & Fine Calculation
- Authentication System
- Unit Testing

---

## Author

Arun