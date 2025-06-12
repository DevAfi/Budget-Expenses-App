from expense import Expense


def main():
    print("Welcome to the Expense Tracker!")
    expense_file = "Expenses.csv"
    ""

    # Take input from user
    e1 = get_user_input()
    # write input to a file
    write_to_file(e1, expense_file)

    
    # Read from the file and display the expenses
    summarize_expenses()
    pass


def get_user_input():
    categories = ["Housing", "Food", "Work", "Entertainment", "Other"]

    eName = input("Enter the name of the expense: ")
    eAmount = float(input("Enter the amount of the expense: "))
    
    while True:
        print("Select the type of expense:")
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")
        

        choice_range = f"[1 - {len(categories)}]"
        choice = input(f"Enter a type of expense between {choice_range}: ")

        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            eType = categories[int(choice) - 1]
            print(f"Expense recorded: {eName}, Type: {eType}, Amount: £{eAmount:.2f}")
            newExpense = Expense(eName, categories[int(choice) - 1], eAmount)
            return newExpense
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(categories)}.")
            continue

    

def write_to_file(expense, filename):
    print(f"Writing {expense} to {filename}")

    with open(filename, "a") as file:
        file.write(f"{expense.name},{expense.type},{expense.amount}\n")

def summarize_expenses():
    pass

if __name__ == "__main__":
    main()

