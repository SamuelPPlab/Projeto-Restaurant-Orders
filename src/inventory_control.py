from os import path


class InventoryControl:

    def __init__(self):
        self.data = []
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

    def order_counter(self, order):
        frequencia = 0
        for item in self.data:
            if item['pedido'] == order:
                frequencia += 1
        return frequencia

    def count_compiler(self):
        menu = list(self.ingredients.keys())
        total_per_item = []
        for item in menu:
            total = self.order_counter(item)
            total_per_item.append((item, total))
        return total_per_item

    def ingredients_per_item(self, total):
        total_ingredients = {}
        for item, count in total:
            ingredients = self.ingredients[item]
            for ingredient in ingredients:
                if ingredient not in total_ingredients:
                    total_ingredients[ingredient] = count
                else:
                    total_ingredients[ingredient] += count
        return(total_ingredients)

    def add_new_order(self, costumer, order, day):
        entry = {'cliente': costumer, 'pedido': order, 'dia': day}
        self.data.append(entry)

    def get_quantities_to_buy(self):
        total_of_orders = self.count_compiler()
        return self.ingredients_per_item(total_of_orders)

        print(total_ingredient_per_item)