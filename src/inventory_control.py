class InventoryControl:
    def __init__(self):
        self.INGREDIENTS = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho', 'tomate'],
            'queijo-quente': ['pao', 'queijo', 'queijo'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'bauru': ['pao', 'queijo', 'presunto', 'tomate'],
            'coxinha': ['massa', 'frango'],
        }
        self.MINIMUM_INVENTORY = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
            'tomate': 50,
        }

        self.to_buy = {
                'pao': 0,
                'carne': 0,
                'queijo': 0,
                'molho': 0,
                'presunto': 0,
                'massa': 0,
                'frango': 0,
                'tomate': 0,
            }

    def add_new_order(self, costumer, order, day):
        available_ingredients = set()
        for ingredient in self.INGREDIENTS[order]:
            if self.MINIMUM_INVENTORY[ingredient] > self.to_buy[ingredient]:
                available_ingredients.add(ingredient)
            else:
                return False

        for available_ingredient in available_ingredients:
            self.to_buy[available_ingredient] += 1

        return True

    def get_quantities_to_buy(self):
        return self.to_buy

    def get_available_dishes(self):
        not_available_ingredients = set()
        for ingredient in self.MINIMUM_INVENTORY.keys():
            if (
                self.MINIMUM_INVENTORY[ingredient] - self.to_buy[ingredient]
                <= 0
            ):
                not_available_ingredients.add(ingredient)

        available_products = set()
        for product_name in self.INGREDIENTS.keys():
            check = any(
                ingredient in self.INGREDIENTS[product_name]
                for ingredient in not_available_ingredients
            )

            print(check)
            if not check:
                available_products.add(product_name)
        return available_products
