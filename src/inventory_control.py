from collections import Counter


class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho", "tomate"],
        "queijo-quente": ["pao", "queijo", "queijo"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "bauru": ["pao", "queijo", "presunto", "tomate"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.inventory = self.MINIMUM_INVENTORY.copy()

    def add_new_order(self, costumer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] > 0:
                self.inventory[ingredient] -= 1
            else:
                return False

    def get_quantities_to_buy(self):
        quantities_to_buy = Counter(self.MINIMUM_INVENTORY.copy())
        quantities_to_buy.subtract(Counter(self.inventory))
        return quantities_to_buy
