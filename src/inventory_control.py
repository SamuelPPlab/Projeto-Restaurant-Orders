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

    def add_new_order(self, costumer, order, day):
        for ingredient in InventoryControl.INGREDIENTS[order]:
            if self.inventory[ingredient] > 0:
                self.inventory[ingredient] -= 1

    def get_quantities_to_buy(self):
        quantities_to_buy = {
            ingredient: self.MINIMUM_INVENTORY[ingredient]
            - self.inventory[ingredient]
            for ingredient in self.inventory.keys()
        }
        return quantities_to_buy
