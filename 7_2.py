###UTF-8###


import json
import os

def load_expenses():
    if os.path.exists('expenses.json'):
        with open('expenses.json', 'r') as file:
            return json.load(file)
    else:
        return []

def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)

def add_expense():
    name = input("Введите название расхода: ")
    amount = float(input("Введите сумму: "))

    return {"name": name, "amount": amount}

def display_expenses(expenses):
    for expense in expenses:
        print(f"{expense['name']}: {expense['amount']}")

def main():
    expenses = load_expenses()

    while True:
        print("\n1. Ввести новый расход")
        print("2. Показать все расходы")
        print("3. Выход")

        choice = input("Выберите действие (1/2/3): ")

        if choice == '1':
            new_expense = add_expense()
            expenses.append(new_expense)
            save_expenses(expenses)
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()
