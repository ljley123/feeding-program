import os

try:
    import msvcrt as m
    def pause():
        print("Press any key to continue...")
        m.getch()
except ImportError:
    def pause():
        input("Press Enter to continue...")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_age():
    while True:
        try:
            age = int(input("Enter child's age: "))
            return age
        except ValueError:
            print("Invalid input. Age must be a number.")

def input_weight():
    while True:
        try:
            weight = float(input("Enter child's weight (kg): "))
            return weight
        except ValueError:
            print("Invalid input. Weight must be a number (e.g. 12.5).")

def add_child_data():
    name = input("Enter child's name: ")
    age = input_age()
    weight = input_weight()
    barangay = input("Enter child's barangay: ")

    with open("children_data.txt", "a") as file:
        file.write(f"{name}|{age}|{weight}|{barangay}\n")

    print("\nChild data added successfully!\n")
    pause()

def show_all_data():
    clear()
    print("----------------")
    print("| All Child Data |")
    print("----------------\n")

    if not os.path.exists("children_data.txt") or os.stat("children_data.txt").st_size == 0:
        print("No child data available.\n")
    else:
        with open("children_data.txt", "r") as file:
            data = file.readlines()

        for i, line in enumerate(data):
            name, age, weight, barangay = line.strip().split('|')
            print(f"[{i + 1}] Name: {name} | Age: {age} | Weight: {weight}kg | Barangay: {barangay}")

    print()
    pause()

def update_child_data():
    clear()
    print("------------------------")
    print("| List of Children |")
    print("------------------------\n")

    if not os.path.exists("children_data.txt") or os.stat("children_data.txt").st_size == 0:
        print("No child data available.\n")
        pause()
        return

    with open("children_data.txt", "r") as file:
        data = file.readlines()

    for i, line in enumerate(data):
        name, age, weight, barangay = line.strip().split('|')
        print(f"[{i + 1}] Name: {name} | Age: {age} | Weight: {weight}kg | Barangay: {barangay}")

    try:
        index = int(input("\nEnter the number of the child you want to update: ")) - 1
        if index < 0 or index >= len(data):
            print("Invalid selection.")
            pause()
            return

        name, age, weight, barangay = data[index].strip().split('|')

        print("\nEnter new values or press Enter to keep existing data.\n")
        new_name = input(f"Name [{name}]: ") or name
        new_age = input(f"Age [{age}]: ") or age
        new_weight = input(f"Weight [{weight}]: ") or weight
        new_barangay = input(f"Barangay [{barangay}]: ") or barangay

        data[index] = f"{new_name}|{new_age}|{new_weight}|{new_barangay}\n"

        with open("children_data.txt", "w") as file:
            file.writelines(data)

        print("\nChild data updated successfully!\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    pause()

def delete():
    clear()
    print("----------------")
    print("| All Child Data |")
    print("----------------\n")

    if not os.path.exists("children_data.txt") or os.stat("children_data.txt").st_size == 0:
        print("No child data available.\n")
        pause()
        return

    with open("children_data.txt", "r") as file:
        data = file.readlines()

    for i, line in enumerate(data):
        name, age, weight, barangay = line.strip().split('|')
        print(f"[{i + 1}] Name: {name} | Age: {age} | Weight: {weight}kg | Barangay: {barangay}")

    try:
        remove_child = int(input("\nEnter number to delete (0 to cancel): ")) - 1
        if remove_child == -1:
            print("Exiting delete operation...")
            pause()
            return
        elif 0 <= remove_child < len(data):
            del data[remove_child]
            with open('children_data.txt', 'w') as file:
                file.writelines(data)
            print("\nChild data deleted successfully.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

    pause()

def main():
    while True:
        clear()
        print("------------------------------------")
        print(" Feeding Program Data Collection ")
        print("------------------------------------\n")
        print("1. Add Child Data")
        print("2. Show All Data")
        print("3. Update Child Data")
        print("4. Delete Child Data")
        print("5. Exit\n")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            clear()
            add_child_data()
        elif choice == "2":
            show_all_data()
        elif choice == "3":
            update_child_data()
        elif choice == "4":
            delete()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("--------------------------------------------")
            print("| Invalid choice. Please select 1 to 5.     |")
            print("--------------------------------------------")
            pause()

main()