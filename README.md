# Personal Finance Tracker  (Intermediate Python Course): 
This project is part of a training course for intermediate level developers and also aimed at those who want to gain practical experience .
The project is a user-friendly tool designed to help individuals efficiently manage their finances. This application enables users to log and categorize their expenses and income, track monthly spending, set savings goals, and view financial reports that offer a clear overview of their financial health. With intuitive features like monthly summaries and category-wise breakdowns, users can easily gain insights into their spending habits and adjust their budgets to meet financial goals.

# Features:

Expense & Income Tracking: Record daily transactions with customizable categories to monitor spending and income sources.

Monthly Reports: Generate monthly summaries that highlight spending patterns and income flow for a comprehensive view of financial activity.

Category-wise Analysis: View detailed analysis of expenses per category (e.g., groceries, transportation, entertainment) to identify major spending areas.

Savings Goals: Set and track personal savings goals to help achieve financial milestones.

Data Visualization: Leverage Matplotlib or Seaborn to present data in easy-to-understand graphs and charts, making financial insights more accessible.

Simple GUI: A user-friendly interface developed with Tkinter for easy navigation and interaction with financial data.

# Skills Used:

File Handling: Use CSV files for easy data export and import.

SQLite Database: Store and manage data locally in a structured and reliable format.

Data Visualization: Create insightful charts using Matplotlib or Seaborn for visual analysis of financial trends.

Tkinter: Build a simple, intuitive graphical user interface that enhances the user experience.

This project is an excellent opportunity to apply essential programming skills, including file handling, data manipulation, database management, and data visualization, within a practical and impactful context.

# Feature Implementation Breakdown

Transaction Tracking:

Create Transaction and Category classes.
Implement SQLite database management with CRUD operations for transactions, storing date, amount, category, and notes.
Monthly Summary Reports:

Generate a monthly report that calculates total income, expenses, and net savings.
Store summaries for quick access, and use them for visual representations.
Category-wise Expense Reports:

Aggregate expenses by category and create pie charts for visual insight.
Savings Goals:

Define a Goal class that holds a target amount and tracks progress.
Display progress in the UI with a bar chart or progress indicator.
CSV Import/Export:

Functions to export transactions and goals to CSV and import them back.
Use pandas for easier manipulation and file handling.
Filtering and Sorting (Could-Have):

Extend database queries to support sorting and filtering by date, category, and amount.
Dashboard View (Could-Have):

Create a summary view with quick statistics like highest expense category and total savings.

# Project Structure
finance_tracker/
│
├── main               # Main application entry point .

├── database          # SQLite database handling .

├── models            # Classes for Transaction, Category, Goal .
 
├── views             # GUI components using tkinter .

├── reports           # Report generation and data aggregation .

├── visualizations    # Matplotlib-based visualizations . 

├── utils.           # Helper functions (e.g., date formatting) . 

└── requirements.txt      # Package requirements . 


# Technologies

SQLite for local, lightweight database storage.
pandas for data importexport (CSV handling).
tkinter for building a GUI interface.
matplotlib for creating bar and pie charts.

# Installation and Setup :

1 - Clone the repository: git clone `https://github.com/mohamedelghazali/Personal-Finance-Tracker` .

2 - Install required dependencies with `pip install -r requirements.txt` .

3 - Run the application with python `main.py` .
