import pandas as pd, os

if os.path.exists("Expenses.csv"):
    dataset = pd.read_csv("Expenses.csv")
else:
    dataset = pd.DataFrame(columns = ["Date", "Category", "Amount", "Type"])

def Add():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))
    data_type = input("Enter the type (Income/Expense): ")
    
    global dataset
    new_entry = pd.DataFrame([[date, category, amount, data_type]], columns = ["Date", "Category", "Amount", "Type"])
    dataset = pd.concat([dataset, new_entry], ignore_index = True)
    print("Transaction added successfully.")

def View():
    if dataset.empty:
        print("No transactions to display.")
    else:
        print("\nSummary of Transactions:")
        print(dataset)
        print("\nTotal Amount: ", dataset["Amount"].sum())


while True:
    print("\nPersonal Expense Tracker \n1. Add Transaction \n2. View Summary \n3. Save & Exit")
    choice = int(input("Your choice: "))
    
    if choice == 1:
        Add()
    elif choice == 2:
        View()
    elif choice == 3:
        dataset.to_csv('Expenses.csv', index = False)
        print("Expenses saved to Expenses.csv. Exiting...")
        break
    else:
        print("Invalid choice, please try again.")