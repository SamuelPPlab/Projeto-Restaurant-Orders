class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho', 'tomate'],
        'queijo-quente': ['pao', 'queijo', 'queijo'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'bauru': ['pao', 'queijo', 'presunto', 'tomate'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.ingredients = self.INGREDIENTS
        self.orders = []
        self.client_dishes = dict()
        self.minimum_inventory = self.MINIMUM_INVENTORY

    def feed_system(self):
        for order in self.orders:
            self.client_dishes[order[0]] = self.client_dishes.get(
                order[0], []
            ) + [order[1]]

    def clear_system(self):
        self.client_dishes.clear()

    def add_new_order(self, costumer, order, day):
        for ingredient in self.ingredients[order]:
            if self.minimum_inventory[ingredient] > 0:
                self.minimum_inventory[ingredient] -= 1
            else:
                return False
        self.orders.append([costumer, order, day])
        self.clear_system()
        self.feed_system()

    def get_quantities_to_buy(self):
        set_ingredients = set(self.minimum_inventory)
        list_ingredients = {item: 0 for item in set_ingredients}
        list_dishes = [item[1] for item in self.orders]
        for dishe in list_dishes:
            for ingredient in self.ingredients[dishe]:
                list_ingredients[ingredient] = (
                    list_ingredients.get(ingredient, 0) + 1
                )
        return list_ingredients

    def get_available_dishes(self):
        dishes_available = set()
        for dishe, ingredients in self.ingredients.items():
            available = False
            for ingredient in ingredients:
                if self.minimum_inventory[ingredient] > 0:
                    available = True
                else:
                    available = False
                    break
            if available:
                dishes_available.add(dishe)
        return dishes_available


# inventario = InventoryControl()
# # inventario.add_new_order("jorge", "hamburguer", "terça-feira")
# # inventario.add_new_order("jorge", "pizza", "terça-feira")
# # inventario.add_new_order("jorge", "coxinha", "terça-feira")
# for _ in range(50):
#     inventario.add_new_order("jorge", "hamburguer", "terça-feira")
# # print(inventario.minimum_inventory)
# print(inventario.get_available_dishes())
