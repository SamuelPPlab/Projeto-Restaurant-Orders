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
        self.__quantities_to_buy = {
            key: 0 for key in self.MINIMUM_INVENTORY.keys()
        }
        self.__ingredients = {
            key: set(ingredients)
            for key, ingredients in self.INGREDIENTS.items()
        }

    def add_new_order(self, costumer, order, day):
        for ingredient in self.__ingredients[order]:
            if ingredient in self.__quantities_to_buy:
                self.__quantities_to_buy[ingredient] += 1
            else:
                self.__quantities_to_buy[ingredient] = 1

    def get_quantities_to_buy(self):
        return self.__quantities_to_buy
