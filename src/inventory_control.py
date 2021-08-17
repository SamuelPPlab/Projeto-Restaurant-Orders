
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
        self.track_orders = []

    def get_available_dishes(self):
        used_ingredients = self.get_quantities_to_buy()
        current_inventory = {}

        for key, value in used_ingredients.items():
            current_inventory[key] = self.MINIMUM_INVENTORY[key] - value

        removed_dishes = set()
        all_dishes = {k for k, v in self.INGREDIENTS.items()}

        for key, value in current_inventory.items():
            if value == 0:
                for k, v in self.INGREDIENTS.items():
                    if key in v:
                        removed_dishes.add(k)

        new_menu = all_dishes.difference(removed_dishes)

        return new_menu

    def add_new_order(self, costumer, order, day):
        used_ingredients = self.get_quantities_to_buy()
        ingredients = list(self.INGREDIENTS[order])

        for item in list(ingredients):
            used_ingredients[item] += 1

        for key, value in used_ingredients.items():
            if (self.MINIMUM_INVENTORY[key] - value) < 0:
                return False
        # self.get_available_dishes()
        self.track_orders.append(list((costumer, order, day)))

        return True

    def get_quantities_to_buy(self):
        ingredients = {x for _, value in self.INGREDIENTS.items()
                       for x in value}
        used_ingredients = {key: 0 for key in ingredients}
        for _, order, _ in self.track_orders:
            for ingredient in self.INGREDIENTS[order]:
                used_ingredients[ingredient] += 1

        return used_ingredients

        # retorno: um conjunto de pratos que ainda têm ingredientes disponíveis


if __name__ == "__main__":
    ingredients = InventoryControl()

    count = 1
    while count <= 50:
        ingredients.add_new_order("jorge", "coxinha", "terça-feira")
        count += 1
    print(ingredients.get_available_dishes())

    # ingredients.add_new_order("jorge", "hamburguer", "terça-feira")
    # # ingredients.add_new_order("jorge", "hamburguer", "terça-feira")
    # # ingredients.add_new_order("jorge", "hamburguer", "terça-feira")
    # hamburguer = ingredients.get_quantities_to_buy()
    # print(hamburguer)
