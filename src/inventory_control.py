class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM = {
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

        self.ordered = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def get_ingredients(self, order):
        return self.INGREDIENTS[order]

    def verify_inventory(self, ingredients):
        for ingredient in ingredients:
            if (self.ordered[ingredient] >= self.MINIMUM[ingredient]):
                return False
        return True

    def add_to_ordered_ingredients(self, ingredients):
        for ingredient in ingredients:
            self.ordered[ingredient] += 1

    def add_new_order(self, costumer, order, day):
        ingredients = self.get_ingredients(order)
        if (self.verify_inventory(ingredients)):
            self.orders.append({
                'costumer': costumer,
                'order': order,
                'day': day,
            })
            self.add_to_ordered_ingredients(ingredients)
        else:
            return False

    def get_quantities_to_buy(self):
        return self.ordered
