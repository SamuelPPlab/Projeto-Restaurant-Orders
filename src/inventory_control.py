from src.track_orders import TrackOrders


class InventoryControl:
    orders = TrackOrders()

    def __init__(self):

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

        self.get_quantities_to_buy = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }

    def add_new_order(self, costumer, order, day):
        index = 0
        ingredients = self.ingredients(order)
        while (
            index < len(ingredients)
            and self.get_quantities_to_buy[ingredients[index]]
            < self.minimum_inventory[ingredients[index]]
        ):
            index += 1
        
        if index == len(ingredients):
            for ingredient in self.ingredients[order]:
                self.get_quantities_to_buy[ingredient] = self.get_quantities_to_buy[ingredient] + 1
        else:
            return False

    def get_quantities_to_buy(self):
        return self.get_quantities_to_buy

    def get_available_dishes(self):
        dishes = self.ingredients.keys()
        available_dishes = []
        for dish in dishes:
            ingredients = self.ingredients[dish]
            index = 0
            while (
                index < len(ingredients)
                and self.get_quantities_to_buy[ingredients[index]]
            ):
                index += 1
            
            if index == len(ingredients):
                available_dishes = [*available_dishes, dish]
            
        return set(available_dishes)
