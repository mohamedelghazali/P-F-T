# finance_tracker.py
from database_setup import create_tables, create_connection
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Model Definitions
class Category:
    @staticmethod
    def add(name):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO categories (name) VALUES (?)', (name,))
        print("Category added successfully.")

    @staticmethod
    def get_all():
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM categories')
            return cursor.fetchall()

class Transaction:
    @staticmethod
    def add(amount, category_id, date, description):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO transactions (amount, category_id, date, description) VALUES (?, ?, ?, ?)',
                           (amount, category_id, date, description))
        print("Transaction added successfully.")

    @staticmethod
    def get_all():
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM transactions')
            return cursor.fetchall()

# Report Generation
def monthly_report(year, month):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT SUM(amount) FROM transactions
                      WHERE strftime('%Y', date) = ? AND strftime('%m', date) = ?''', (year, month))
    total_spent = cursor.fetchone()[0] or 0
    return total_spent

def category_report():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''SELECT categories.name, SUM(transactions.amount) 
                      FROM transactions 
                      JOIN categories ON transactions.category_id = categories.id 
                      GROUP BY categories.name''')
    return cursor.fetchall()

# Data Visualization
def visualize_expenses_by_category():
    data = category_report()
    categories = [d[0] for d in data]
    amounts = [d[1] for d in data]

    plt.figure(figsize=(10, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expenses by Category")
    plt.show()

def visualize_monthly_expenses(year, month):
    total_spent = monthly_report(year, month)
    plt.bar([f"{year}-{month}"], [total_spent])
    plt.title("Monthly Expense Summary")
    plt.xlabel("Month")
    plt.ylabel("Total Expenses")
    plt.show()

# GUI Setup
def add_transaction():
    amount = float(amount_entry.get())
    category_name = category_entry.get()
    date = date_entry.get()
    description = description_entry.get()

    # Add category if it doesn't exist
    Category.add(category_name)
    category_id = Category.get_all()[-1][0]  # Get last added category ID

    # Add transaction
    Transaction.add(amount, category_id, date, description)
    messagebox.showinfo("Success", "Transaction added!")

def create_gui():
    global amount_entry, category_entry, date_entry, description_entry
    root = tk.Tk()
    root.title("Personal Finance Tracker")

    tk.Label(root, text="Amount").grid(row=0, column=0)
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=0, column=1)

    tk.Label(root, text="Category").grid(row=1, column=0)
    category_entry = tk.Entry(root)
    category_entry.grid(row=1, column=1)

    tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=2, column=0)
    date_entry = tk.Entry(root)
    date_entry.grid(row=2, column=1)

    tk.Label(root, text="Description").grid(row=3, column=0)
    description_entry = tk.Entry(root)
    description_entry.grid(row=3, column=1)

    tk.Button(root, text="Add Transaction", command=add_transaction).grid(row=4, column=1)
    tk.Button(root, text="Show Category Report", command=visualize_expenses_by_category).grid(row=5, column=1)
    root.mainloop()

if __name__ == "__main__":
    create_tables()
    create_gui()
