import random
import os

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Name: {self.name}\nBalance: {self.balance}\nAccount Number: {self.account_number}"

class Bank:
    def __init__(self, filename="accounts.txt"):
        self.filename = filename
        self.accounts = []
        self.load_from_file()

    def generate_unique_account_number(self):
        existing_numbers = {acc.account_number for acc in self.accounts}
        while True:
            number = random.randint(1000, 1999)
            if number not in existing_numbers:
                return number

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit must be non-negative.")
            return

        account_number = self.generate_unique_account_number()
        account = Account(account_number, name, initial_deposit)
        self.accounts.append(account)

        with open(self.filename, 'a') as file:
            file.write(f"{account.account_number}, {account.name}, {account.balance}\n")

        print(f"\nAccount created successfully! Your account number is {account_number}")
        print("-" * 51)

    def view_account(self, account_number):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split(', ')
                        if int(parts[0]) == account_number:
                            print("\nAccount Found:")
                            print(f"Account Number: {parts[0]}")
                            print(f"Name: {parts[1]}")
                            print(f"Balance: {parts[2]}")
                            print("-" * 51)
                            return
                print("Account Not Found")
        except FileNotFoundError:
            print("No accounts file found")
        except Exception as e:
            print(f"Error reading account data: {e}")
        print("-" * 51)

    def deposit(self):
        try:
            account_number = int(input("Enter account number: "))
            deposit_amount = float(input("Enter amount to deposit: "))
            if deposit_amount <= 0:
                print("Deposit amount must be positive.")
                return

            account_found = False
            updated_lines = []

            with open(self.filename, 'r') as file:
                lines = file.readlines()

            for line in lines:
                if line.strip():
                    parts = line.strip().split(', ')
                    if int(parts[0]) == account_number:
                        new_balance = float(parts[2]) + deposit_amount
                        parts[2] = str(new_balance)
                        account_found = True
                        print(f"Deposit successful! New balance: {new_balance}")
                    updated_lines.append(', '.join(parts) + '\n')

            with open(self.filename, 'w') as file:
                file.writelines(updated_lines)

            if not account_found:
                print("Such account doesn't exist")

        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {e}")
        print("-" * 51)

    def withdraw(self):
        try:
            account_number = int(input("Enter account number: "))
            withdraw_amount = float(input("Enter amount to withdraw: "))
            if withdraw_amount <= 0:
                print("Withdrawal amount must be positive.")
                return

            account_found = False
            updated_lines = []

            with open(self.filename, 'r') as file:
                lines = file.readlines()

            for line in lines:
                if line.strip():
                    parts = line.strip().split(', ')
                    if int(parts[0]) == account_number:
                        current_balance = float(parts[2])
                        if withdraw_amount > current_balance:
                            print("Insufficient funds!")
                        else:
                            new_balance = current_balance - withdraw_amount
                            parts[2] = str(new_balance)
                            account_found = True
                            print(f"Withdrawal successful! New balance: {new_balance}")
                    updated_lines.append(', '.join(parts) + '\n')

            with open(self.filename, 'w') as file:
                file.writelines(updated_lines)

            if not account_found:
                print("Such account doesn't exist")

        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {e}")
        print("-" * 51)

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split(', ')
                        account = Account(int(parts[0]), parts[1], float(parts[2]))
                        self.accounts.append(account)
        except Exception as e:
            print(f"Error loading accounts: {e}")

    def main_page(self):
        print("Welcome to SimpleBank 🏦")
        print("-" * 51)
        print("1. Create New Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        while True:
            try:
                print()
                user_input = int(input("Select an option: "))
                if user_input == 1:
                    name = input("Enter your full name: ")
                    initial_deposit = float(input("Enter initial deposit: "))
                    self.create_account(name, initial_deposit)
                elif user_input == 2:
                    acc_num = int(input("Enter account number: "))
                    self.view_account(acc_num)
                elif user_input == 3:
                    self.deposit()
                elif user_input == 4:
                    self.withdraw()
                elif user_input == 5:
                    print("Saving data and exiting... Goodbye!")
                    break
                else:
                    print("Invalid option. Please select 1–5.")
            except ValueError:
                print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    bank = Bank()
    bank.main_page()
