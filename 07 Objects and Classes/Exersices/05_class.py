class Inventory:
    __capacity = 0
    items = []

    def __init__(self, capacity: int):
        Inventory.__capacity = capacity

    def add_item(self, item: str):
        if len(Inventory.items) < Inventory.__capacity:
            Inventory.items.append(item)

        return "not enough room in the inventory"

    def get_capacity(self):
        return Inventory.__capacity

    def __repr__(self):
        return f"Items: {', '.join(Inventory.items)}.\nCapacity left: {Inventory.__capacity - len(Inventory.items)}"