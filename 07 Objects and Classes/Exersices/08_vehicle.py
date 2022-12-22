class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        self.money = money

        if self.owner is not None and money >= self.price:
            self.owner = owner
            change = self.money - self.price
            return f"Successfully bought a {self.type}. Change: {change}"
        elif money < self.price:
            return "Sorry, not enough money"
        else:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"
