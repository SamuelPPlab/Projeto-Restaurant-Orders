from os import initgroups, path


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
            'pao': 1,
            'carne': 50,
            'queijo': 5,
            'molho': 50,
            'presunto': 3,
            'massa': 50,
            'frango': 50,
        }
        self.available_dishes = []

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
    
    def get_available_dishes(self, pedido):
        ingredients = self.ingredients[pedido]
        is_available = []
        for ingredient in ingredients:
            quantity = self.minimum_inventory[ingredient]
            is_available.append(not quantity > 0)
        if not any(is_available):
            return True
        return False
