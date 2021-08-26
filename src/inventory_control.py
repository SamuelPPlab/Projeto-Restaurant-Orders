from collections import Counter


class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.recipes = dict(self.INGREDIENTS)
        self.inventory = dict(self.MINIMUM_INVENTORY)

    def add_new_order(self, costumer, order, day):
        for item in self.recipes[order]:
            if self.inventory[item] > 0:
                self.inventory[item] -= 1
            else:
                return False

    def get_quantities_to_buy(self):
        itens_to_buy = Counter(self.MINIMUM_INVENTORY) - Counter(
            self.inventory
        )
        for i in itens_to_buy:
            if itens_to_buy[i] == 0:
                itens_to_buy.pop(i)
        return itens_to_buy
