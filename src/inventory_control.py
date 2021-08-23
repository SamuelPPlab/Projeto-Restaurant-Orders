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
        self.inventory = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }
        self.dishes = {'hamburguer', 'pizza', 'misto-quente', 'coxinha'}

    def get_available_dishes(self):
        available_dishes = set()
        used_ingredients = self.get_quantities_to_buy()
        unavailable_ingredients = set()

        for ingredient in used_ingredients:
            total_ingredient = self.MINIMUM_INVENTORY[ingredient]
            ingredient_count = total_ingredient - used_ingredients[ingredient]
            if ingredient_count == 0:
                unavailable_ingredients.add(ingredient)

        for dish in self.dishes:
            if all(
                ingredient in
                used_ingredients for
                ingredient in
                self.INGREDIENTS[dish]
            ) and not any(
                ingredient in
                unavailable_ingredients for
                ingredient in
                self.INGREDIENTS[dish]
            ):
                available_dishes.add(dish)

        return available_dishes

    def add_new_order(self, costumer, order, day):
        ingredients = self.INGREDIENTS[order]

        for ingredient in ingredients:
            self.inventory[ingredient] += 1

            order_ingredients = self.inventory.values()
            max_ingredients = self.MINIMUM_INVENTORY.values()

            index = 0

            for value in order_ingredients:

                if value > list(max_ingredients)[index]:
                    return False

                index += 1

        self.orders.append(list((costumer, order, day)))
        return True

    def get_quantities_to_buy(self):
        return self.inventory
