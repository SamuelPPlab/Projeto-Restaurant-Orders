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
        self.inventory = dict(self.MINIMUM_INVENTORY)
        # from:
        # https://stackoverflow.com/questions/16819222/how-to-return-dictionary-keys-as-a-list-in-python
        self.available_dishes = {*self.INGREDIENTS}

    def add_new_order(self, costumer, order, day):
        for ingredient in InventoryControl.INGREDIENTS[order]:
            if self.inventory[ingredient] > 0:
                self.inventory[ingredient] -= 1
            else:
                return False

    def get_quantities_to_buy(self):
        quantities_to_buy = {
            ingredient: self.MINIMUM_INVENTORY[ingredient]
            - self.inventory[ingredient]
            for ingredient in self.inventory.keys()
        }
        return quantities_to_buy

    def get_available_dishes(self):
        avaliable_ingredients = {
            ingredient
            for ingredient in self.inventory
            if self.inventory.get(ingredient) > 0
        }

        for dish in self.INGREDIENTS:
            dish_ingredients = set(self.INGREDIENTS[dish])
            if not avaliable_ingredients.issuperset(dish_ingredients):
                self.available_dishes.discard(dish)
        return self.available_dishes
