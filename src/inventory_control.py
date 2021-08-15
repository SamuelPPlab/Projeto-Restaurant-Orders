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


class InventoryControl:
    def __init__(self):
        self.__quantities_to_buy = {key: 0 for key in MINIMUM_INVENTORY.keys()}
        self.__foods = {
            key: set(ingredients) for key, ingredients in INGREDIENTS.items()
        }
        self.__inventory = {
            key: quantity for key, quantity in MINIMUM_INVENTORY.items()
        }
        self.__menu = set(INGREDIENTS.keys())

    def __add_quantities_to_buy(self, ingredient):
        self.__quantities_to_buy[ingredient] += 1

    def __decrement_ingredient_from_inventry(self, ingredient):
        self.__inventory[ingredient] -= 1

    def __update_menu(self, ingredient):
        if self.__inventory[ingredient] <= 0:
            for food, ingredients in self.__foods.items():
                if ingredient in ingredients:
                    self.__menu.discard(food)

    def add_new_order(self, _costumer, order, _day):
        if order in self.__menu:
            for ingredient in self.__foods[order]:
                self.__add_quantities_to_buy(ingredient)
                self.__decrement_ingredient_from_inventry(ingredient)
                self.__update_menu(ingredient)
        else:
            return False

    def get_quantities_to_buy(self):
        return self.__quantities_to_buy

    def get_available_dishes(self):
        return self.__menu
