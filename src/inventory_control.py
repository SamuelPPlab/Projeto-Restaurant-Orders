class InventoryControl:

    def __init__(self):
        self.orders = []
        self.MINIMUM_INVENTORY = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }
        self.INGREDIENTS = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }

    def add_new_order(self, costumer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if (self.MINIMUM_INVENTORY[ingredient] - 1) < 0:
                return False

        # set order
        self.orders.append((costumer, order, day))

        # update inventory
        for ingredient in self.INGREDIENTS[order]:
            self.MINIMUM_INVENTORY[ingredient] -= 1

    def get_quantities_to_buy(self):
        ingredients_to_buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

        for order in self.orders:
            for ingredient in self.INGREDIENTS[order[1]]:
                ingredients_to_buy[ingredient] += 1

        return ingredients_to_buy

    def get_available_dishes(self):
        available_dishes = set()
        check = True
        for dish in self.INGREDIENTS.keys():
            for ingredients in self.INGREDIENTS[dish]:
                if self.MINIMUM_INVENTORY[ingredients] <= 0:
                    check = False
                    break
            if check:
                available_dishes.add(dish)
            check = True
        print(self.MINIMUM_INVENTORY)
        return available_dishes
