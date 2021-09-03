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
        """Este copy 👇 - não sei pra que.
        Mas todo mundo usou. E passou no teste.
        """
        self.inventory = self.MINIMUM_INVENTORY.copy()

    def add_new_order(self, costumer, order, day):
        for item in self.INGREDIENTS[order]:
            if self.inventory[item] < 1:
                return False
            self.inventory[item] -= 1

    def get_quantities_to_buy(self):
        buy_list = dict()

        for item in self.inventory:
            total = self.MINIMUM_INVENTORY[item] - self.inventory[item]
            buy_list[item] = total
        return buy_list

    def get_available_dishes(self):
        list_dishes = self.INGREDIENTS.keys()
        for ingredient, quantity in self.inventory.items():
            if quantity == 0:
                list_dishes = [
                    dish
                    for dish in list_dishes
                    if ingredient not in self.INGREDIENTS[dish]
                ]

        self.INGREDIENTS = set(list_dishes)
        return self.INGREDIENTS
