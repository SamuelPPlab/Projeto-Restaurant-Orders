class InventoryControl:

    def __init__(self):
        self.data = []
        self.available_dishes = []
        self.MINIMUM_INVENTORY = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }
        self.INGREDIENTS = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }

    def inventory_tracker(self, pedido):
        ingredients = self.INGREDIENTS[pedido]
        for item in ingredients:
            if self.MINIMUM_INVENTORY[item] > 0:
                self.MINIMUM_INVENTORY[item] -= 1
                return True
            else:
                return False

    def order_counter(self, order):
        frequencia = 0
        for item in self.data:
            if item['pedido'] == order:
                frequencia += 1
        return frequencia

    def count_compiler(self):
        menu = list(self.INGREDIENTS.keys())
        total_per_item = []
        for item in menu:
            total = self.order_counter(item)
            total_per_item.append((item, total))
        return total_per_item

    def ingredients_per_item(self, total):
        total_ingredients = {}
        for item, count in total:
            ingredients = self.INGREDIENTS[item]
            for ingredient in ingredients:
                if ingredient not in total_ingredients:
                    total_ingredients[ingredient] = count
                else:
                    total_ingredients[ingredient] += count
        return(total_ingredients)

    def add_new_order(self, costumer, order, day):
        ingredient_missing = self.inventory_tracker(order)
        if not ingredient_missing:
            return False
        else:
            entry = {'cliente': costumer, 'pedido': order, 'dia': day}
            self.data.append(entry)

    def get_quantities_to_buy(self):
        total_of_orders = self.count_compiler()
        print(self.MINIMUM_INVENTORY)
        return self.ingredients_per_item(total_of_orders)

    def removes_item_from_available(self, item, is_available):
        menu_and_ingredients = list(self.INGREDIENTS.items())
        for ingredient in menu_and_ingredients:
            if item in ingredient[1]:
                try:
                    is_available.remove(ingredient[0])
                except ValueError:
                    pass
        return is_available

    def get_available_dishes(self):
        ingredients = list(self.MINIMUM_INVENTORY.keys())
        is_available = list(self.INGREDIENTS.keys())
        out_of_stock = []
        for ingredient in ingredients:
            quantity = self.MINIMUM_INVENTORY[ingredient]
            if quantity < 1:
                out_of_stock.append(ingredient)
        for item in out_of_stock:
            is_available = self.removes_item_from_available(item, is_available)
        return set(is_available)
