import os

# File where expenses will be saved permanently
DATA_FILE = "expenses.txt"

def display_menu():
    print("\n========= SpendWise Menu =========")
    print("1. Add an Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")
    print("==================================")

def add_expense():
    item = input("Enter the item name (e.g., Book, Lunch): ")
    try:
        amount = float(input("Enter the amount spent: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    category = input("Enter category (e.g., Education, Food, Travel): ")

    # Open the text file in append mode ('a') to add the data to the end
    with open(DATA_FILE, "a") as file:
        file.write(f"{item},{amount},{category}\n")
    
    print(f"🎉 Successfully added expense for {item}!")

def view_expenses():
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        print("\n📭 No expenses recorded yet!")
        return

    print("\n--- Your Expenses ---")
    print(f"{'Item':<15} | {'Amount':<10} | {'Category':<15}")
    print("-" * 45)
    
    with open(DATA_FILE, "r") as file:
        for line in file:
            # Split the line by commas to read individual data tokens
            item, amount, category = line.strip().split(",")
            print(f"{item:<15} | ${float(amount):<10.2f} | {category:<15}")

def view_total():
    if not os.path.exists(DATA_FILE):
        print("\nTotal Spending: $0.00")
        return

    total = 0.0
    with open(DATA_FILE, "r") as file:
        for line in file:
            item, amount, category = line.strip().split(",")
            total += float(amount)
            
    print(f"\n💰 Total Cumulative Spending: ${total:.2f}")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            print("\nThank you for using SpendWise! Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option from the menu.")

if __name__ == "__main__":
    main()
