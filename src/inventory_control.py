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
        self.inventory = self.MINIMUM_INVENTORY.copy()

    def add_new_order(self, costumer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] > 0:
                self.inventory[ingredient] -= 1
            else:
                return False

    def get_quantities_to_buy(self):
        quantity_to_buy = Counter(self.MINIMUM_INVENTORY.copy())
        quantity_in_inventory = Counter(self.inventory)
        quantity_to_buy.subtract(quantity_in_inventory)
        return quantity_to_buy

    def get_available_dishes(self):
        ingredients = []
        available_meals = []
        for ingredient in self.inventory:
            ingredients.append(ingredient)
            if self.inventory[ingredient] > 0:
                for meal in self.INGREDIENTS:
                    if set(self.INGREDIENTS[meal]).issubset(ingredients):
                        available_meals.append(meal)
        return set(available_meals)
