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

    def get_available_dishes(self):
        recipes_to_remove = set()
        for meal in self.recipes:
            for ingredient in self.recipes[meal]:
                if self.inventory[ingredient] == 0:
                    recipes_to_remove.add(meal)
        for meal in recipes_to_remove:
            self.recipes.pop(meal)
        return self.recipes.keys()

    def add_new_order(self, costumer, order, day):
        self.get_available_dishes()
        try:
            for item in self.recipes[order]:
                if self.inventory[item] > 0:
                    self.inventory[item] -= 1
        except(AssertionError):
            return False

    def get_quantities_to_buy(self):
        itens_to_buy = Counter(self.MINIMUM_INVENTORY) - Counter(
            self.inventory
        )
        for i in self.inventory:
            if i not in itens_to_buy:
                itens_to_buy.update({i: 0})

        return itens_to_buy
