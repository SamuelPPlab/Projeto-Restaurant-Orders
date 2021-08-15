class InventoryControl:
    def __init__(self):
        self.stock = []

        self.ingredients = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }

        self.minimum_inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }

        self.control = self.minimum_inventory.copy()

    def add_new_order(self, costumer, order, day):
        items_food = self.ingredients[order]
        if len(self.stock) == 0:
            self.stock.append([costumer, order, day])
            for item in items_food:
                self.control[item] -= 1
        else:
            for item in items_food:
                self.control[item] -= 1
                if self.control[item] < 0:
                    return False
            self.stock.append([costumer, order, day])

    def get_quantities_to_buy(self):
        total_ingredients = self.minimum_inventory.copy()
        for ing in total_ingredients:
            total_ingredients[ing] = 0
        for food in self.stock:
            ingredients = self.ingredients[food[1]]
            for item in ingredients:
                total_ingredients[item] += 1
        return total_ingredients

    def get_available_dishes(self):
        items_used = self.get_quantities_to_buy()
        inventory = self.minimum_inventory

        set_foods = set(self.ingredients)
        items_finished = set()

        for item in items_used:
            if inventory[item] <= items_used[item]:
                items_finished.add(item)
        for item in self.ingredients:
            set_contain = items_finished.isdisjoint(self.ingredients[item])
            if item in set_foods and not set_contain:
                set_foods.remove(item)
        return set_foods

# inventory = InventoryControl()
# count = 1
# while count <= 50:
#     inventory.add_new_order("maria", "hamburguer", "sexta")
#     inventory.add_new_order("maria", "coxinha", "sexta")
#     inventory.add_new_order("maria", "misto-quente", "sexta")
#     print(inventory.add_new_order("maria", "coxinha", "sexta"))
#     count += 1
