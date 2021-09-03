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
        self.INVENTORY = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }

    def add_new_order(self, costumer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.INVENTORY[ingredient] - 1 < 0:
                return False
            self.INVENTORY[ingredient] -= 1

        self.orders.append([costumer, order, day])

        return True

    def get_quantities_to_buy(self):
        shoppingList = {}
        for i in self.MINIMUM_INVENTORY:
            shoppingList[i] = self.MINIMUM_INVENTORY[i] - self.INVENTORY[i]

        return shoppingList

    def get_available_dishes(self):
        availableDishes = set()
        for dish in self.INGREDIENTS:
            for i in self.INGREDIENTS[dish]:
                if self.INVENTORY[i] == 0:
                    break
            else:
                availableDishes.add(dish)

        return availableDishes
