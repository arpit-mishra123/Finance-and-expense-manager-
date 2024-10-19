from datetime import datetime

class Expense:
    def __init__(self, amount, category, description, date=None):
        self.amount = amount
        self.category = category
        self.description = description
        # If no date is provided, use the current date
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def __repr__(self):
        return f"{self.date} | {self.category} | ${self.amount} | {self.description}"
import pandas as pd

# Function to save expenses to a CSV file
def save_expense_to_csv(expense, filename='expenses.csv'):
    data = {
        'Date': [expense.date],
        'Category': [expense.category],
        'Amount': [expense.amount],
        'Description': [expense.description]
    }
    df = pd.DataFrame(data)

    # Append the new expense to the file if it exists; create the file otherwise
    df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)

# Example usage
expense = Expense(50, 'Groceries', 'Bought vegetables')
save_expense_to_csv(expense)
# Function to load expenses from the CSV file
def load_expenses(filename='expenses.csv'):
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print("No expense data found.")
        return pd.DataFrame()

# Function to display expenses
def display_expenses(df):
    if df.empty:
        print("No expenses recorded yet.")
    else:
        print(df)

# Example usage
df = load_expenses()
display_expenses(df)
def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date (YYYY-MM-DD) or press Enter for today's date: ")
        expense = Expense(amount, category, description, date if date else None)
        save_expense_to_csv(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input! Please enter valid data.")
def delete_expense():
    df = load_expenses()
    display_expenses(df)
    
    if not df.empty:
        try:
            index = int(input("Enter the index of the expense to delete: "))
            df = df.drop(index, axis=0)
            df.to_csv('expenses.csv', index=False)
            print("Expense deleted successfully!")
        except ValueError:
            print("Invalid index.")

# Example usage
delete_expense()
# Summarize expenses by category
def summarize_by_category():
    df = load_expenses()
    if not df.empty:
        summary = df.groupby('Category')['Amount'].sum()
        print(summary)
    else:
        print("No expenses recorded yet.")

# Summarize expenses by month
def summarize_by_month():
    df = load_expenses()
    if not df.empty:
        df['Date'] = pd.to_datetime(df['Date'])
        summary = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum()
        print(summary)
    else:
        print("No expenses recorded yet.")
import matplotlib.pyplot as plt

# Function to visualize expenses by category
def visualize_expenses_by_category():
    df = load_expenses()
    if not df.empty:
        summary = df.groupby('Category')['Amount'].sum()
        summary.plot(kind='pie', autopct='%1.1f%%')
        plt.title('Expenses by Category')
        plt.ylabel('')
        plt.show()

# Function to visualize expenses by month
def visualize_expenses_by_month():
    df = load_expenses()
    if not df.empty:
        df['Date'] = pd.to_datetime(df['Date'])
        summary = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum()
        summary.plot(kind='bar', color='skyblue')
        plt.title('Monthly Expenses')
        plt.ylabel('Amount')
        plt.xlabel('Month')
        plt.show()
def main_menu():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Summarize Expenses by Category")
        print("5. Summarize Expenses by Month")
        print("6. Visualize Expenses by Category")
        print("7. Visualize Expenses by Month")
        print("8. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            df = load_expenses()
            display_expenses(df)
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            summarize_by_category()
        elif choice == '5':
            summarize_by_month()
        elif choice == '6':
            visualize_expenses_by_category()
        elif choice == '7':
            visualize_expenses_by_month()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()

