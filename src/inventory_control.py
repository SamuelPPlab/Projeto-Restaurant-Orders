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
        self.orders = []
        self.quantity_to_buy = self.MINIMUM_INVENTORY
        for element in self.quantity_to_buy.keys():
            self.quantity_to_buy[element] = 0

    def add_new_order(self, costumer, order, day):
        self.orders.append({'client': costumer, 'order': order, 'day': day})
        for element in self.INGREDIENTS[order]:
            self.quantity_to_buy[element] += 1

    def get_quantities_to_buy(self):
        return self.quantity_to_buy
