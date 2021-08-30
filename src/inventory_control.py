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
            self.storage[item] -= 1

    def get_quantities_to_buy(self):
        quantities = dict()
        for item in self.storage:
            result = self.MINIMUM_INVENTORY[item] - self.storage[item]
            quantities[item] = result
        return quantities
