class Vehicle:
    def __init__(self, type, model, price, owner =None ):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self,money: int, owner: str):
        self.money = money
        change = abs(self.money - self.price)
        if self.owner is not None:
            if money >= self.price and self.owner == None:
                self.owner = owner

                return f"Successfully bought a {self.type}. Change: {change}"
            elif money < self.price:
                return "Sorry, not enough money"
        else:
            return "Vehicle has no owner"

    def sell(self):
        pass

    def __repr__(self):
        return  f"{model} {type} is owned by: {owner}".
        return  f"{model} {type} is on sale: {price}"