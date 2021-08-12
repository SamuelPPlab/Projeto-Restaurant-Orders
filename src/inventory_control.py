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
        self.menu = self.INGREDIENTS.copy()
        self.current_inventory_orders = self.MINIMUM_INVENTORY.copy()
        self.costs_inventory_orders = {
            ingredient: 0 for ingredient in self.MINIMUM_INVENTORY.keys()
        }

    def add_new_order(self, _costumer, order, _day):
        for item in self.INGREDIENTS[order]:
            if self.current_inventory_orders[item] < 1:
                return False
            self.costs_inventory_orders[item] += 1
            self.current_inventory_orders[item] -= 1

    def get_quantities_to_buy(self):
        return self.costs_inventory_orders

    def get_available_dishes(self):
        new_menu = self.menu.keys()
        for ingredient, count in self.current_inventory_orders.items():
            if count == 0:
                new_menu = [
                    dish
                    for dish in new_menu
                    if ingredient not in self.menu[dish]
                ]
        self.menu = set(new_menu)
        return self.menu


if __name__ == "__main__":
    ingredients = InventoryControl()
    count = 1
    while count <= 50:
        ingredients.add_new_order("jorge", "coxinha", "terça-feira")
        count += 1
    ingredients.add_new_order("jorge", "coxinha", "terça-feira")
    print(ingredients.get_quantities_to_buy())
    print(ingredients.get_available_dishes())
