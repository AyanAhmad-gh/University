from person import Person
from pharmacy_system import PharmacySystem

class Customer(Person):
    def __init__(self):
        self.system = PharmacySystem()


    def buy_medicine(self):
        name = input("Enter medicine name: ")
        quantity = int(input("Enter quantity: "))
        if self.system.check_availability(name, quantity):
            self.system.sell_medicine(name, quantity)
            print(f"Purchased {quantity} units of {name}.")
        else:
            print(f"Sorry, {name} is not available in the desired quantity.")
