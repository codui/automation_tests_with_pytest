# Вспомогательный класс
class ShoppingCart:
    def __init__(self) -> None:
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def get_total_price(self):
        return sum(self.items.values())
