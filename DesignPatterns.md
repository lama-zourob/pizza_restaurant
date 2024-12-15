# DesignPatterns.md

## Design Patterns in the Pizza Restaurant System

### Singleton Pattern

#### Description
The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance.

#### Application in the System
The `InventoryManager` class uses the Singleton pattern to manage ingredient availability. Only one inventory manager exists in the system, ensuring consistent tracking of inventory across all pizza orders.

#### Before Applying the Pattern
Without the Singleton pattern, multiple instances of the `InventoryManager` class could exist, leading to inconsistencies in tracking ingredient availability.

#### After Applying the Pattern
By using the Singleton pattern, a single instance of `InventoryManager` is shared across the entire system. This ensures that ingredient availability is updated consistently.

#### Code Example
```python
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
```

### Decorator Pattern

#### Description
The Decorator pattern dynamically adds behavior to an object without altering its structure.

#### Application in the System
Toppings (Cheese, Olives, Mushrooms) are implemented using the Decorator pattern. Each topping adds its cost and description to the base pizza dynamically.

#### Before Applying the Pattern
Each combination of base pizza and toppings would require a separate class, leading to an explosion of classes and reduced maintainability.

#### After Applying the Pattern
The Decorator pattern allows toppings to be added dynamically, reducing the number of required classes and improving maintainability.

#### Code Example
```python
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()

class Cheese(ToppingDecorator):
    def get_description(self):
        return f"{self.pizza.get_description()}, Cheese"

    def get_cost(self):
        return self.pizza.get_cost() + 1.0
```

### Strategy Pattern

#### Description
The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.

#### Application in the System
The Strategy pattern is used to implement payment methods. Different payment strategies (e.g., PayPal, Credit Card) can be selected dynamically at runtime.

#### Before Applying the Pattern
Payment logic would be tightly coupled to the pizza ordering system, making it difficult to add new payment methods.

#### After Applying the Pattern
The Strategy pattern decouples payment logic from the main system, making it easy to add new payment methods.

#### Code Example
```python
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")
```

### Overengineering

#### Concept
Overengineering occurs when a system is designed with excessive complexity, incorporating features or patterns that are unnecessary for the current requirements.

#### Example in the Pizza Restaurant Project
Adding a Factory pattern for toppings when the current system only has three toppings would be overengineering. The current implementation using the Decorator pattern is sufficient.

#### Code Example
```python

class ToppingFactory:
    @staticmethod
    def create_topping(name, pizza):
        if name == "Cheese":
            return Cheese(pizza)
        elif name == "Olives":
            return Olives(pizza)
        elif name == "Mushrooms":
            return Mushrooms(pizza)
        else:
            raise ValueError("Unknown topping")
```

