from collections import Counter


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

    def get_available_dishes(self):
        available_dishes = set()
        for ingredient, inventory_list in self.INGREDIENTS.items():
            flag = True
            for inventory in inventory_list:
                if self.inventory[inventory] <= 0:
                    flag = False
            if flag:
                available_dishes.add(ingredient)
        return available_dishes

    def __init__(self):
        self.inventory = self.MINIMUM_INVENTORY.copy()

    def add_new_order(self, costumer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] > 0:
                self.inventory[ingredient] -= 1
            else:
                return False

    def get_quantities_to_buy(self):
        quantities_to_buy = Counter(self.MINIMUM_INVENTORY.copy())
        quantities_to_buy.subtract(Counter(self.inventory))
        return quantities_to_buy
