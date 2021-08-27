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
        self.storage = self.MINIMUM_INVENTORY.copy()

    def add_new_order(self, _costumer, order, _day):
        for item in self.INGREDIENTS[order]:
            if self.storage[item] < 1:
                return False
            self.storage[item] -= 1

    def get_quantities_to_buy(self):
        quantities = dict()
        for item in self.storage:
            result = self.MINIMUM_INVENTORY[item] - self.storage[item]
            quantities[item] = result
        return quantities

    def get_available_dishes(self):
        menu = self.INGREDIENTS.keys()
        for ingredient, count in self.storage.items():
            if count == 0:
                menu = [
                    dish
                    for dish in menu
                    if ingredient not in self.INGREDIENTS[dish]
                ]
        self.INGREDIENTS = set(menu)
        return self.INGREDIENTS
