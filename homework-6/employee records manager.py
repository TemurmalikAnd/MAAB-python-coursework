import os

def main_menu():
    """Main menu for the Employee Records Manager"""
    print("""
=== Employee Records Manager ===
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")
    
    try:
        user_input = int(input("Go to: "))
        if user_input == 1:
            add_employee()
        elif user_input == 2:
            view_records()
        elif user_input == 3:
            search_employee()
        elif user_input == 4:
            update_employee()
        elif user_input == 5:
            delete_employee()
        elif user_input == 6:
            print("Goodbye!")
            exit()
        else:
            print("Invalid option. Please choose 1-6.")
            main_menu()
    except ValueError:
        print("Please enter a valid number.")
        main_menu()

def add_employee():
    """Add a new employee record to the file"""
    try:
        print("Please enter employee details:")
        emp_id = input("Employee ID: ").strip()
        if not emp_id:
            print("Employee ID cannot be empty.")
            return_to_menu_or_retry(add_employee)
            return
            
        # Check if employee ID already exists
        if employee_exists(emp_id):
            print(f"Employee with ID '{emp_id}' already exists.")
            return_to_menu_or_retry(add_employee)
            return
            
        name = input("Name: ").strip()
        position = input("Position: ").strip()
        salary = input("Salary: ").strip()
        
        if not all([name, position, salary]):
            print("All fields are required.")
            return_to_menu_or_retry(add_employee)
            return
        
        # Create the record
        record = f"{emp_id}, {name}, {position}, {salary}\n"
        
        with open("employees.txt", 'a') as f:
            f.write(record)
        
        print("Employee record added successfully ✅")
        return_to_menu_or_retry(add_employee)
        
    except Exception as e:
        print(f"Error adding employee: {e}")
        return_to_menu_or_retry(add_employee)

def view_records():
    """Display all employee records"""
    try:
        if not os.path.exists("employees.txt"):
            print("No employee records found. The file doesn't exist yet.")
            return_to_menu_or_retry(view_records)
            return
            
        with open("employees.txt", "r") as f:
            content = f.read().strip()
            
        if not content:
            print("No employee records found. The file is empty.")
        else:
            print("\n=== All Employee Records ===")
            print("Employee ID, Name, Position, Salary")
            print("-" * 40)
            print(content)
            
        return_to_menu_or_retry(view_records)
        
    except Exception as e:
        print(f"Error reading records: {e}")
        return_to_menu_or_retry(view_records)

def search_employee():
    """Search for an employee by Employee ID"""
    try:
        if not os.path.exists("employees.txt"):
            print("No employee records found.")
            return_to_menu_or_retry(search_employee)
            return
            
        search_id = input("Enter Employee ID to search: ").strip()
        if not search_id:
            print("Employee ID cannot be empty.")
            return_to_menu_or_retry(search_employee)
            return
            
        with open("employees.txt", 'r') as f:
            lines = f.readlines()
        
        found = False
        for line in lines:
            line = line.strip()
            if line and line.startswith(search_id + ","):
                print(f"\nEmployee found:")
                print(f"Record: {line}")
                found = True
                break
                
        if not found:
            print(f"Employee with ID '{search_id}' not found.")
            
        return_to_menu_or_retry(search_employee)
        
    except Exception as e:
        print(f"Error searching for employee: {e}")
        return_to_menu_or_retry(search_employee)

def update_employee():
    """Update an employee's information"""
    try:
        if not os.path.exists("employees.txt"):
            print("No employee records found.")
            return_to_menu_or_retry(update_employee)
            return
            
        with open("employees.txt", 'r') as f:
            lines = f.readlines()
        
        if not lines:
            print("No employee records found.")
            return_to_menu_or_retry(update_employee)
            return
            
        search_id = input("Enter Employee ID to update: ").strip()
        if not search_id:
            print("Employee ID cannot be empty.")
            return_to_menu_or_retry(update_employee)
            return
            
        found = False
        for i, line in enumerate(lines):
            line = line.strip()
            if line and line.startswith(search_id + ","):
                print(f"\nCurrent record: {line}")
                
                # Parse current record
                try:
                    parts = [part.strip() for part in line.split(',')]
                    if len(parts) != 4:
                        print("Invalid record format. Skipping this record.")
                        continue
                        
                    current_id, current_name, current_position, current_salary = parts
                    
                    # Get new information
                    print(f"\nEnter new information (press Enter to keep current value):")
                    new_name = input(f"Name [{current_name}]: ").strip() or current_name
                    new_position = input(f"Position [{current_position}]: ").strip() or current_position
                    new_salary = input(f"Salary [{current_salary}]: ").strip() or current_salary
                    
                    # Update the line
                    lines[i] = f"{search_id}, {new_name}, {new_position}, {new_salary}\n"
                    found = True
                    break
                    
                except ValueError:
                    print("Error parsing record. Invalid format.")
                    continue
                    
        if not found:
            print(f"Employee with ID '{search_id}' not found.")
            return_to_menu_or_retry(update_employee)
            return
        
        # Write the updated lines back to the file
        with open("employees.txt", 'w') as f:
            f.writelines(lines)
        
        print("Employee record updated successfully ✅")
        return_to_menu_or_retry(update_employee)
        
    except Exception as e:
        print(f"Error updating employee: {e}")
        return_to_menu_or_retry(update_employee)

def delete_employee():
    """Delete an employee record"""
    try:
        if not os.path.exists("employees.txt"):
            print("No employee records found.")
            return_to_menu_or_retry(delete_employee)
            return
            
        with open("employees.txt", 'r') as f:
            lines = f.readlines()
        
        if not lines:
            print("No employee records found.")
            return_to_menu_or_retry(delete_employee)
            return
            
        search_id = input("Enter Employee ID to delete: ").strip()
        if not search_id:
            print("Employee ID cannot be empty.")
            return_to_menu_or_retry(delete_employee)
            return
            
        found = False
        for i, line in enumerate(lines):
            line_stripped = line.strip()
            if line_stripped and line_stripped.startswith(search_id + ","):
                print(f"\nRecord to delete: {line_stripped}")
                
                # Confirm deletion
                confirm = input("Are you sure you want to delete this record? (y/N): ").strip().lower()
                if confirm == 'y':
                    del lines[i]
                    found = True
                    print("Record deleted successfully ✅")
                else:
                    print("Deletion cancelled.")
                    return_to_menu_or_retry(delete_employee)
                    return
                break
                
        if not found:
            print(f"Employee with ID '{search_id}' not found.")
            return_to_menu_or_retry(delete_employee)
            return
        
        # Write the updated lines back to the file
        with open("employees.txt", 'w') as f:
            f.writelines(lines)
            
        return_to_menu_or_retry(delete_employee)
        
    except Exception as e:
        print(f"Error deleting employee: {e}")
        return_to_menu_or_retry(delete_employee)

def employee_exists(emp_id):
    """Check if an employee ID already exists"""
    try:
        if not os.path.exists("employees.txt"):
            return False
            
        with open("employees.txt", 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            if line and line.startswith(emp_id + ","):
                return True
        return False
        
    except Exception:
        return False

def return_to_menu_or_retry(current_function):
    """Helper function to handle return to menu or retry logic"""
    try:
        user_input = input("\nReturn to main menu? (Y/n): ").strip().lower()
        if user_input in ['y', 'yes', '']:
            main_menu()
        else:
            current_function()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        exit()

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        exit()