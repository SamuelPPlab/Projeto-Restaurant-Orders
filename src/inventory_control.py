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
        self.dishes = InventoryControl.INGREDIENTS
        self.min_inventory = InventoryControl.MINIMUM_INVENTORY
        self.inventory = {
          'pao': 50,
          'carne': 50,
          'queijo': 100,
          'molho': 50,
          'presunto': 50,
          'massa': 50,
          'frango': 50,
        }

    def add_new_order(self, costumer, order, day):
        for ingredient in self.dishes[order]:
            if self.inventory[ingredient] > 0:
                self.inventory[ingredient] -= 1
            else:
                return False

    def get_quantities_to_buy(self):
        to_buy_list = {}
        for item in self.inventory:
            to_buy_list[item] = self.min_inventory[item] - self.inventory[item]
        return to_buy_list

    def get_available_dishes(self):
        available_ingredients = set()
        available_dishes = set()
        for ingredient in self.inventory:
            if self.inventory[ingredient] > 0:
                available_ingredients.add(ingredient)
        for dish in self.dishes:
            if set(self.dishes[dish]).intersection(
              available_ingredients) == set(self.dishes[dish]):
                available_dishes.add(dish)
        return available_dishes
