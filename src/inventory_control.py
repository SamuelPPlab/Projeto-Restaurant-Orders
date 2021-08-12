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
        self.current_inventory_orders = self.MINIMUM_INVENTORY.copy()
        self.costs_inventory_orders = {
            ingredient: 0 for ingredient in self.MINIMUM_INVENTORY.keys()
        }

    def add_new_order(self, costumer, order, day):
        ingredients = self.INGREDIENTS[order]
        for item in ingredients:
            if self.current_inventory_orders[item] == 0:
                return False
            self.costs_inventory_orders[item] += 1
            self.current_inventory_orders[item] -= 1

    def get_quantities_to_buy(self):
        return self.costs_inventory_orders


if __name__ == "__main__":
    inventory = InventoryControl()
    count = 1
    while count <= 30:
        inventory.add_new_order("jorge", "hamburguer", "terça-feira")
        count += 1

    print(inventory.add_new_order("jorge", "hamburguer", "terça-feira"))
    print(inventory.get_quantities_to_buy())
    print(inventory.current_inventory_orders)

    new_inventory = InventoryControl()
    print(new_inventory.current_inventory_orders)
