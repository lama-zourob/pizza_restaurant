# Singleton Inventory Manager
class InventoryManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._inventory = {
            "Margherita": 10,
            "Pepperoni": 10,
            "Cheese": 15,
            "Olives": 10,
            "Mushrooms": 12,
        }

    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory


# Pizza classes and decorators
class Pizza:
    def __init__(self, description, cost):
        self._description = description
        self._cost = cost

    def get_description(self):
        return self._description

    def get_cost(self):
        return self._cost


class Margherita(Pizza):
    def __init__(self):
        super().__init__("Margherita", 5.0)


class Pepperoni(Pizza):
    def __init__(self):
        super().__init__("Pepperoni", 6.0)


class ToppingDecorator(Pizza):
    def __init__(self, pizza, topping_description, topping_cost):
        self._pizza = pizza
        self._topping_description = topping_description
        self._topping_cost = topping_cost

    def get_description(self):
        return f"{self._pizza.get_description()} + {self._topping_description}"

    def get_cost(self):
        return self._pizza.get_cost() + self._topping_cost


class Cheese(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Cheese", 1.0)


class Olives(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Olives", 0.5)


class Mushrooms(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Mushrooms", 0.7)


# Payment classes
class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError("This method should be overridden in subclasses.")


class PayPal(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using PayPal.")


class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using Credit Card.")


# Main function
def main():
    inventory_manager = InventoryManager()

    print("Welcome to the Pizza Restaurant!")

    while True:
        print("\nChoose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => Exit")
        pizza_choice = input("Enter the number of your choice: ")

        if pizza_choice == "0":
            break

        # Create pizza base
        if pizza_choice == "1":
            if inventory_manager.check_and_decrement("Margherita"):
                pizza = Margherita()
            else:
                print("Sorry, Margherita is out of stock.")
                continue
        elif pizza_choice == "2":
            if inventory_manager.check_and_decrement("Pepperoni"):
                pizza = Pepperoni()
            else:
                print("Sorry, Pepperoni is out of stock.")
                continue
        else:
            print("Invalid choice.")
            continue

        # Add toppings
        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            if topping_choice == "1":
                if inventory_manager.check_and_decrement("Cheese"):
                    pizza = Cheese(pizza)
                else:
                    print("Sorry, Cheese is out of stock.")
            elif topping_choice == "2":
                if inventory_manager.check_and_decrement("Olives"):
                    pizza = Olives(pizza)
                else:
                    print("Sorry, Olives are out of stock.")
            elif topping_choice == "3":
                if inventory_manager.check_and_decrement("Mushrooms"):
                    pizza = Mushrooms(pizza)
                else:
                    print("Sorry, Mushrooms are out of stock.")
            elif topping_choice == "4":
                break
            else:
                print("Invalid choice.")

        # Display final pizza details
        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        # Payment
        print("\nChoose payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter the number of your choice: ")

        if payment_choice == "1":
            payment_method = PayPal()
        elif payment_choice == "2":
            payment_method = CreditCard()
        else:
            print("Invalid payment method.")
            continue

        payment_method.pay(pizza.get_cost())

        # Show final inventory
        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())


if __name__ == "__main__":
    main()
