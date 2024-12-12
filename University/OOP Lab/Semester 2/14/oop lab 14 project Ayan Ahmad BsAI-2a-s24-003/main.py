# main.py
from pharmacist import Pharmacist
from customer import Customer

def main_menu():
    while True:
        print("\nWelcome to Pharmacy Management System")
        user_type = input("Are you a Pharmacist or Customer? (Enter P or C): ").strip().lower()

        if user_type == "p":
            name = input("Enter your name: ")
            employee_id = input("Enter your employee ID: ")
            user = Pharmacist(name, employee_id)

            while True:
                print("\nPharmacist Menu")
                print("1. Add Medicine")
                print("2. View Stock")
                print("3. Register Premises")
                print("4. View Premises")
                print("5. Exit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    med_name = input("Enter medicine name: ")
                    med_type = input("Enter medicine type (Tablet, Syrup, etc.): ")
                    quantity = int(input("Enter quantity: "))
                    price = float(input("Enter price: "))
                    user.system.add_medicine(med_name, med_type, quantity, price)
                elif choice == "2":
                    user.system.show_stock()
                elif choice == "3":
                    premises_name = input("Enter premises name: ")
                    address = input("Enter address: ")
                    user.system.register_premises(premises_name, address)
                elif choice == "4":
                    user.system.show_premises()
                elif choice == "5":
                    break
                else:
                    print("Invalid choice. Try again.")

        elif user_type == "c":
            while True:
                print("\nCustomer Menu")
                print("1. Buy Medicine")
                print("2. Exit")
                choice = input("Enter your choice: ")

                if choice == "1":
                    med_name = input("Enter medicine name: ")
                    quantity = int(input("Enter quantity: "))
                    if user.system.sell_medicine(med_name, quantity):
                        print(f"Purchased {quantity} units of {med_name}.")
                    else:
                        print(f"Sorry, {med_name} is not available in the desired quantity.")
                elif choice == "2":
                    break
                else:
                    print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
