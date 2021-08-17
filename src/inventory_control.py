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

    def add_new_order(self, costumer, order, day):
        self.track_orders.append(list((costumer, order, day)))

    def get_quantities_to_buy(self):
        used_ingredients = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0, }
        for _, order, _ in self.track_orders:
            for ingredient in self.INGREDIENTS[order]:
                if used_ingredients[ingredient] > self.MINIMUM_INVENTORY[ingredient]:
                    return False
                used_ingredients[ingredient] += 1
        return used_ingredients


if __name__ == "__main__":
    ingredients = InventoryControl()
    count = 1
    while count <= 50:
        ingredients.add_new_order("jorge", "hamburguer", "terça-feira")
        count += 1

    hamburguer = ingredients.get_quantities_to_buy()
    print(hamburguer)
