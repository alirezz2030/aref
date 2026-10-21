import sqlite3
from datetime import date


DB_NAME = "expenses.db"


def create_database():
    with sqlite3.connect(DB_NAME) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                amount REAL NOT NULL CHECK (amount > 0),
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )
        """)


create_database()
print("Database is ready!")




def add_expense(title, amount, category, expense_date):
    with sqlite3.connect(DB_NAME) as connection:
        connection.execute("""
            INSERT INTO expenses (title, amount, category, date)
            VALUES (?, ?, ?, ?)
        """, (title, amount, category, expense_date))

    print("Expense added successfully!")


# add_expense(
#     "Python Book",
#     250000,
#     "Education",
#     "2026-10-17"
# )




def show_expenses():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.execute("""
            SELECT id, title, amount, category, date
            FROM expenses
            ORDER BY date DESC, id DESC
        """)

        expenses = cursor.fetchall()

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(
            f"ID: {expense[0]} | "
            f"Title: {expense[1]} | "
            f"Amount: {expense[2]:,.0f} | "
            f"Category: {expense[3]} | "
            f"Date: {expense[4]}"
        )



def filter_by_category(category):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.execute("""
            SELECT title, amount, date
            FROM expenses
            WHERE category = ?
            ORDER BY date DESC
        """, (category,))

        expenses = cursor.fetchall()

    if not expenses:
        print("No expenses found in this category.")
        return

    for expense in expenses:
        print(
            f"{expense[0]} | "
            f"{expense[1]:,.0f} | "
            f"{expense[2]}"
        )


# filter_by_category("Education")



def show_total_expenses():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.execute(
            "SELECT SUM(amount) FROM expenses"
        )

        total = cursor.fetchone()[0]

    total = total or 0
    print(f"Total expenses: {total:,.0f}")



def category_report():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.execute("""
            SELECT category, SUM(amount), COUNT(*)
            FROM expenses
            GROUP BY category
            ORDER BY SUM(amount) DESC
        """)

        report = cursor.fetchall()

    if not report:
        print("No data available.")
        return

    for category, total, count in report:
        print(
            f"{category}: {total:,.0f} "
            f"({count} transactions)"
        )


def get_positive_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")



def get_date():
    while True:
        value = input("Enter date (YYYY-MM-DD), or press Enter for today: ")

        if not value:
            return date.today().isoformat()

        try:
            parsed_date = date.fromisoformat(value)
            return parsed_date.isoformat()

        except ValueError:
            print("Invalid date. Example: 2026-10-17")





def main():
    create_database()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. Show all expenses")
        print("3. Filter by category")
        print("4. Show total expenses")
        print("5. Category report")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Enter title: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue

            amount = get_positive_amount()
            category = input("Enter category: ").strip()

            if not category:
                print("Category cannot be empty.")
                continue

            expense_date = get_date()

            try:
                add_expense(title, amount, category, expense_date)
            except sqlite3.IntegrityError as error:
                print("Could not save expense:", error)

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            category = input("Enter category: ").strip()
            filter_by_category(category)

        elif choice == "4":
            show_total_expenses()

        elif choice == "5":
            category_report()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Choose from 1 to 6.")


if __name__ == "__main__":
    main()