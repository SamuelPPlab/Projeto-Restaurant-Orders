class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.inventory = self.MINIMUM_INVENTORY.copy()

    def add_new_order(self, costumer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] > 0:
                self.inventory[ingredient] -= 1
            else:
                return False

    def get_quantities_to_buy(self):
        return {
            ingredient: self.MINIMUM_INVENTORY[ingredient]
            - self.inventory.get(ingredient, 0)
            for ingredient in self.MINIMUM_INVENTORY.keys()
        }

    def get_available_dishes(self):
        available_ingredients = set(
            ingredient
            for ingredient in self.inventory
            if self.inventory[ingredient] > 0
        )
        return {
            dish
            for dish in self.INGREDIENTS
            if set(self.INGREDIENTS[dish]).issubset(available_ingredients)
        }
