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
        ingredients_list = self.INGREDIENTS[order]
        for ingredient in ingredients_list:
            if self.storage[ingredient] > 0:
                self.storage[ingredient] -= 1
            else:
                return False

    def get_quantities_to_buy(self):
        quantities_to_buy = dict()
        for item in self.storage:
            balance = self.MINIMUM_INVENTORY[item] - self.storage[item]
            quantities_to_buy[item] = balance
        return quantities_to_buy

    def get_available_dishes(self):
        available_dishes = set()
        for product in self.INGREDIENTS:
            ingredients = self.INGREDIENTS[product]
            flag = True
            for ingredient in ingredients:
                if self.storage[ingredient] < 1:
                    flag = False
                    break
            if flag:
                available_dishes.add(product)
        return available_dishes
