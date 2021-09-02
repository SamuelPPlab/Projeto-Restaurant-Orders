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

# Idéia do PR da colega Letícia
# (https://github.com/tryber/sd-07-restaurant-orders/tree/leticia-ferreira-project-name)
    def __init__(self):
        self.inventory = self.MINIMUM_INVENTORY.copy()

    def add_new_order(self, _costumer, order, _day):
        for item in self.INGREDIENTS[order]:
            if self.inventory[item] < 1:
                return False
            self.inventory[item] -= 1

    def get_quantities_to_buy(self):
        quantities_to_buy = dict()

        for item in self.inventory:
            result_to_buy = self.MINIMUM_INVENTORY[item] - self.inventory[item]
            quantities_to_buy[item] = result_to_buy

        return quantities_to_buy

    def get_available_dishes(self):
        list_foods = self.INGREDIENTS.keys()

        for ingredient, count in self.inventory.items():
            if count == 0:
                list_foods = [
                    dish
                    for dish in list_foods
                    if ingredient not in self.INGREDIENTS[dish]
                ]

        self.INGREDIENTS = set(list_foods)
        return self.INGREDIENTS
