from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

BOOKS_CSV = BASE_DIR / "data_base" / "books_data.csv"
MEMBERS_CSV = BASE_DIR / "data_base" / "members_data.csv"
BORROW_LOG_CSV = BASE_DIR / "data_base" / "borrow_log.csv"