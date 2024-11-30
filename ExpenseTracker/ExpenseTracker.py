import pandas as pd, os

if os.path.exists("Expenses.csv"):
    dataset = pd.read_csv("Expenses.csv")
else:
    dataset = pd.DataFrame(columns = ["Date", "Category", "Amount", "Type"])

def Add():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))
    transaction_type = int(input("Enter the number of the type (Income = 0 / Expense = 1): "))

    if transaction_type == 1:
        transaction_type = "Expense"
    elif transaction_type == 0:
        transaction_type = "Income"
    else:
        print("Invalid transaction type. \nOperation cancelled.")
        return
    
    global dataset
    new_entry = pd.DataFrame([[date, category, amount, transaction_type]], columns = ["Date", "Category", "Amount", "Type"])
    dataset = pd.concat([dataset, new_entry], ignore_index = True)
    print("Transaction added successfully.")

def View():
    if dataset.empty:
        print("No transactions to display.")
    else:
        print("\nSummary of Transactions:")
        print(dataset)
        
        total_income = dataset.loc[dataset["Type"] == "Income", "Amount"].sum()
        total_expense = dataset.loc[dataset["Type"] == "Expense", "Amount"].sum()
        net_total = total_income - total_expense
        
        print("\nTotal Income: ", total_income)
        print("Total Expenses: ", total_expense)
        print("Net Total: ", net_total)

def Edit():
    if dataset.empty:
        print("No transactions to edit.")
        return

    print("Current Transactions:")
    print(dataset)

    index = int(input("Enter the index of the transaction you want to edit (Enter -1 to cancel this operation): "))

    if 0 <= index < len(dataset):
        print("Editing Transaction at index:", index)
        
        new_date = input(f"Enter the new date (Current: {dataset.at[index, 'Date']}): ") or dataset.at[index, "Date"]
        new_category = input(f"Enter the new category (Current: {dataset.at[index, "Category"]}): ") or dataset.at[index, "Category"]
        new_amount = input(f"Enter the new amount (Current: {dataset.at[index, "Amount"]}): ")
        new_transaction_type = input(f"Enter the new type (Current: {dataset.at[index, "Type"]})) (Income = 0 / Expense = 1): ")

        if not new_amount:
            dataset.at[index, "Amount"]
        else:
            new_amount = float(new_amount)

        if new_transaction_type == "1":
            new_transaction_type = "Expense"
        elif new_transaction_type == "0":
            new_transaction_type = "Income"
        else:
            new_transaction_type = dataset.at[index, "Type"]

        dataset.at[index, "Date"] = new_date
        dataset.at[index, "Category"] = new_category
        dataset.at[index, "Amount"] = new_amount
        dataset.at[index, "Type"] = new_transaction_type

        print("Transaction updated successfully.")
    elif index == -1:
        print("Operation cancelled.")
        return
    else:
        print("Invalid index. No transaction edited.")

def Delete():
    if dataset.empty:
        print("No transactions to delete.")
        return
    
    print("Current Transactions:")
    print(dataset)
    
    index = int(input("Enter the index of the transaction you want to delete (Enter -1 to cancel this operation): "))
    
    if 0 <= index < len(dataset):
        dataset.drop(index, inplace = True)
        dataset.reset_index(drop = True, inplace = True)
        print("Transaction deleted successfully.")
    elif index == -1:
        print("Operation cancelled.")
    else:
        print("Invalid index. No transaction deleted.")

while True:
    print("\nPersonal Expense Tracker \n1. Add Transaction \n2. Edit Transaction \n3. Delete Transaction \n4. View Summary \n5. Save & Exit")
    choice = int(input("Enter the number of your choice: "))
    
    if choice == 1:
        Add()
    elif choice == 2:
        Edit()
    elif choice == 3:
        Delete()
    elif choice == 4:
        View()
    elif choice == 5:
        dataset.to_csv('Expenses.csv', index = False)
        print("Expenses saved to Expenses.csv. Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
