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

        self.__current_inventory = {
            "pao": 50,
            "carne": 50,
            "queijo": 100,
            "molho": 50,
            "presunto": 50,
            "massa": 50,
            "frango": 50,
        }

    def add_new_order(self, costumer, order, day):
        available_dishes = self.get_available_dishes()
        if order not in available_dishes:
            return False
        for ingredient in self.ingredients[order]:
            self.__current_inventory[ingredient] -= 1

    def get_quantities_to_buy(self):
        purchase_list = {}
        for ingredient in self.minimum_inventory:
            purchase_list[ingredient] = (
                self.minimum_inventory[ingredient]
                - self.__current_inventory[ingredient]
            )
        return purchase_list

    def get_available_dishes(self):
        available_dishes = {dish for dish in self.ingredients}
        absent_ingredients = {
            ingredient
            for ingredient in self.__current_inventory
            if self.__current_inventory[ingredient] < 1
        }
        for dish, ingredients in self.ingredients.items():
            for absent in absent_ingredients:
                if absent in ingredients:
                    available_dishes.discard(dish)
        return available_dishes
