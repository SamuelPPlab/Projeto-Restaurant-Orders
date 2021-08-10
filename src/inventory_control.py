class InventoryControl:
    def __init__(self):
        self.ingredients = {
            "hamburguer": ["pao", "carne", "queijo"],
            "pizza": ["massa", "queijo", "molho"],
            "misto-quente": ["pao", "queijo", "presunto"],
            "coxinha": ["massa", "frango"],
        }

        self.minimum_inventory = {
            "pao": 50,
            "carne": 50,
            "queijo": 100,
            "molho": 50,
            "presunto": 50,
            "massa": 50,
            "frango": 50,
        }

        self.inventory = {
            "pao": 50,
            "carne": 50,
            "queijo": 100,
            "molho": 50,
            "presunto": 50,
            "massa": 50,
            "frango": 50,
        }

    def get_all_dishes(self):
        return {dish for dish in self.ingredients}

    def get_unavailable_ingredients(self):
        unavailable_ingredients = {
            ingredient
            for ingredient in self.inventory
            if self.inventory[ingredient] < 1
        }
        return unavailable_ingredients

    # https://www.w3schools.com/python/ref_set_discard.asp

    def get_available_dishes(self):
        available_dishes = self.get_all_dishes()
        unavailable_ingredients = self.get_unavailable_ingredients()

        for dish, ingredients in self.ingredients.items():
            for unavailable in unavailable_ingredients:
                if unavailable in ingredients:
                    available_dishes.discard(dish)

        return available_dishes

    def add_new_order(self, costumer, order, day):
        available_dishes = self.get_available_dishes()
        if order in available_dishes:
            for ingredient in self.ingredients[order]:
                self.inventory[ingredient] -= 1
        return False

    def get_quantities_to_buy(self):
        list = {}
        for ingredient in self.minimum_inventory:
            list[ingredient] = (
                self.minimum_inventory[ingredient] - self.inventory[ingredient]
            )
        return list
