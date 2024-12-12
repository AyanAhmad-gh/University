from person import Person
from pharmacy_system import PharmacySystem

class Pharmacist(Person):
    def __init__(self, name, employee_id):
        super().__init__(name, "Pharmacist")
        self.employee_id = employee_id
        self.system = PharmacySystem()

    def show_details(self):
        print(f"Pharmacist: {self.name}, ID: {self.employee_id}")

    def add_medicine(self):
        name = input("Enter medicine name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        self.system.add_medicine(name, quantity, price)
        print(f"{quantity} units of {name} added successfully!")

    def view_stock(self):
        self.system.show_stock()
