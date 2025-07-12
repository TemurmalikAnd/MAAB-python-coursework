def main_menu():
    print("""
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")
    """
    Option 1: Append a new employee record to "employees.txt".
    Option 2: Display all employee records from "employees.txt".
    Option 3: Allow the user to search for an employee by Employee ID and display their details.
    Option 4: Update an employee’s information (name, position, or salary) based on the Employee ID.
    Option 5: Delete an employee's record from the file using the Employee ID.
    Option 6: Exit the program.
"""
    user_input = int(input("Go to: "))
    if user_input == 1:
        add_employee()
    elif user_input == 2:
        view_records()
    elif user_input == 3:
        search_id()
    elif user_input == 4:
        search_id()
    elif user_input == 5:
        delete_record()
    else:
        exit()

def add_employee():
    with open("employees.txt", 'a') as f:
        print("Employee record should be in the format: Employee ID, Name, Position, Salary")
        new_employee = input("New employee: ")
        f.write(f"\n\n{new_employee}")
        print("Added a new employee ✅")
        user_input = input("Return? (Y/n): ")
        if user_input == 'Y':
            main_menu()
        else:
            add_employee()

def view_records():
    with open("employees.txt", "r") as f:
        print(f.read())
    user_input = input("Return? (Y/n): ")
    if user_input == 'Y':
        main_menu()
    else:
        view_records()

def search_id():
    try:
        with open("employees.txt", 'r') as f:
            search_input = input("Search for: ")
            found = False
            for line in f:
                if search_input in line:
                    print(line.strip())  # Print the entire line
                    found = True
            if not found:
                print("Not exist")
            
        user_input = input("Return? (Y/n): ")
        if user_input == 'Y' or user_input == 'y':
            main_menu()
        else:
            search_id()
    except ValueError:
        print("Employee id can't be a string")
    except FileNotFoundError:
        print("File not found")

def search_id():
    try:
        with open("employees.txt", 'r') as f:
            lines = f.readlines()
        search_input = input("Enter Employee ID to update: ")
        found = False
        for i, line in enumerate(lines):
            if search_input in line:
                print(f"Current record: {line.strip()}")
                found = True
                # Get new information
                new_name = input(f"Enter new name (press Enter to keep '{line.split(', ')[1]}'): ") or line.split(', ')[1]
                new_position = input(f"Enter new position (press Enter to keep '{line.split(', ')[2]}'): ") or line.split(', ')[2]
                new_salary = input(f"Enter new salary (press Enter to keep '{line.split(', ')[3]}'): ") or line.split(', ')[3]
                # Update the line
                lines[i] = f"{search_input}, {new_name}, {new_position}, {new_salary}\n"
                break
        if not found:
            print("Employee not found")

        # Write the updated lines back to the file
        with open("employees.txt", 'w') as f:
            f.writelines(lines)

        user_input = input("Return? (Y/n): ")
        if user_input.lower() == 'y':
            main_menu()
        else:
            search_id()
    except ValueError:
        print("Employee ID can't be a string")
    except FileNotFoundError:
        print("File not found")
    except IndexError:
        print("Invalid record format")
def delete_record():
    try:
        with open("employees.txt", 'r') as f:
            lines = f.readlines()
        search_input = input("Search for: ")
        found = False
        for i, line in enumerate(lines):
            if search_input in line:
                print(f"Deleting record: {line.strip()}")
                del lines[i]
                found = True
                break
        if not found:
            print("Employee not found")

        # Write the updated lines back to the file
        with open("employees.txt", 'w') as f:
            f.writelines(lines)

        user_input = input("Return? (Y/n): ")
        if user_input.lower() == 'y':
            main_menu()
        else:
            delete_record()
    except ValueError:
        print("Employee ID can't be a string")
    except FileNotFoundError:
        print("File not found")
main_menu()