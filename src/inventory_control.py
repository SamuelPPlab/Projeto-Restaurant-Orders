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
        self.__inventory = self.MINIMUM_INVENTORY
        self.__ingredients = {
            key: set(ingredients)
            for key, ingredients in self.INGREDIENTS.items()
        }

    def add_new_order(self, costumer, order, day):
        for ingredient in self.__ingredients[order]:
            self.__inventory[ingredient] -= 1

    def get_quantities_to_buy(self):
        return self.__inventory
