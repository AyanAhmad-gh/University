import csv
import os
from datetime import datetime

class PharmacySystem:
    def __init__(self):
        self.stock_file = "data/stock.csv"
        self.premises_file = "data/premises.csv"
        self.purchase_log_file = "data/purchase_log.csv"
        self.medicine_stock = self.load_data()

    def load_data(self):
        stock = {}
        if os.path.exists(self.stock_file):
            with open(self.stock_file, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    stock[row["name"]] = {
                        "type": row["type"],
                        "quantity": int(row["quantity"]),
                        "price": float(row["price"]),
                    }
        return stock

    def save_data(self):
        with open(self.stock_file, "w", newline="") as file:
            fieldnames = ["name", "type", "quantity", "price"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for name, details in self.medicine_stock.items():
                writer.writerow({
                    "name": name,
                    "type": details["type"],
                    "quantity": details["quantity"],
                    "price": details["price"],
                })

    def add_medicine(self, name, med_type, quantity, price):
        if name in self.medicine_stock:
            self.medicine_stock[name]["quantity"] += quantity
        else:
            self.medicine_stock[name] = {"type": med_type, "quantity": quantity, "price": price}
        self.save_data()

    def show_stock(self):
        if not self.medicine_stock:
            print("No stock available.")
            return
        print("Current Stock:")
        print(f"{'Name':<15} {'Type':<10} {'Quantity':<10} {'Price':<10}")
        print("-" * 45)
        for name, details in self.medicine_stock.items():
            print(f"{name:<15} {details['type']:<10} {details['quantity']:<10} ${details['price']:<10.2f}")

    def check_availability(self, name, quantity):
        if name in self.medicine_stock and self.medicine_stock[name]["quantity"] >= quantity:
            return True
        return False

    def sell_medicine(self, name, quantity):
        if name in self.medicine_stock and self.medicine_stock[name]["quantity"] >= quantity:
            # Update stock
            self.medicine_stock[name]["quantity"] -= quantity
            if self.medicine_stock[name]["quantity"] == 0:
                del self.medicine_stock[name]
            self.save_data()

            # Log the purchase
            self.log_purchase(name, quantity)
            return True
        return False

    def log_purchase(self, medicine_name, quantity):
        with open(self.purchase_log_file, "a", newline="") as file:
            fieldnames = ["medicine_name", "quantity", "date_time"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if os.stat(self.purchase_log_file).st_size == 0:
                writer.writeheader()
            writer.writerow({
                "medicine_name": medicine_name,
                "quantity": quantity,
                "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            })

    def register_premises(self, premises_name, address):
        with open(self.premises_file, "a", newline="") as file:
            fieldnames = ["premises_name", "address"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if os.stat(self.premises_file).st_size == 0:
                writer.writeheader()
            writer.writerow({"premises_name": premises_name, "address": address})

    def show_premises(self):
        if not os.path.exists(self.premises_file):
            print("No premises registered.")
            return
        print("Registered Premises:")
        with open(self.premises_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"{row['premises_name']}: {row['address']}")
