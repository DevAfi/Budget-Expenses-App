from expense import Expense
import datetime
import calendar

def main():
    print("Welcome to the Expense Tracker!")
    expense_file = "Expenses.csv"
    Monthly_budget = 4000

    # Take input from user
    e1 = get_user_input()
    # write input to a file
    write_to_file(e1, expense_file)

    
    # Read from the file and display the expenses
    summarize_expenses(expense_file, Monthly_budget)
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
            #print(f"Expense recorded: {eName}, Type: {eType}, Amount: £{eAmount:.2f}")
            newExpense = Expense(eName, categories[int(choice) - 1], eAmount)
            return newExpense
        else:
            print(f"Invalid choice. Please enter a number between 1 and {len(categories)}.")
            continue

    

def write_to_file(expense, filename):
    #print(f"Writing {expense} to {filename}")

    with open(filename, "a") as file:
        file.write(f"{expense.name},{expense.type},{expense.amount}\n")

def summarize_expenses(filename, budget):
    expense_List = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for single_line in lines:
            stripped = single_line.strip()
            Ename, Etype, Eamount = stripped.split(",")
            line_Expense = Expense(
                name=Ename, type=Etype, amount=float(Eamount)
            )
            #print(line_Expense)
            expense_List.append(line_Expense)


    ppc = {}
    for expense in expense_List:
        key = expense.type
        if key in ppc:
            ppc[key] += expense.amount
        else:
            ppc[key] = expense.amount
    
    print("\nExpense Summary:")
    for key, value in ppc.items():
        print(f"{key}: £{value:.2f}")

    total_expense = sum(expense.amount for expense in expense_List)
    budget_remaining = budget - total_expense
    print(f"\nTotal Expenses: £{total_expense:.2f}")
    if total_expense > budget:
        print(f"Warning: You have exceeded your budget of £{budget:.2f} by £{total_expense - budget:.2f}.")
    else:
        print(f"Total spent: £{total_expense:.2f}")
        print(f"Remaining: £{budget_remaining:.2f}")
    
    current = datetime.datetime.now()
    dIM = calendar.monthrange(current.year, current.month)[1]
    remDays = dIM - current.day
    print("Daily budget: " f"£{budget_remaining / remDays:.2f}")



if __name__ == "__main__":
    main()