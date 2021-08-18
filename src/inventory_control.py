class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
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
        self.orders = []
        self.ingredients = []
        self.inventory = []
        self.ingredients_orders = {}
        for k, v in self.INGREDIENTS.items():
            self.ingredients.append((k, v))
        self.inventory.append(self.MINIMUM_INVENTORY)

    def add_new_order(self, costumer, order, day):
        return self.orders.append({'a': costumer, 'b': order, 'c': day})

    # def inf_orders(self):
    #     for i in self.orders:
    #         if i['b'] in self.ingredients_orders:
    #             self.ingredients_orders[i['b']] += 1
    #         else:
    #             self.ingredients_orders[i['b']] = 1

    # def inf_ingredients(self):
    #     self.inf_orders()
    #     dict = {}
    #     ingredientes = []
    #     for k, v in self.ingredients_orders.items():
    #         for index in self.ingredients:
    #             if k == index[0]:
    #                 ingredientes.append(index[1])
    #     for value in ingredientes:
    #         for value_i in value:
    #             if value_i not in dict:
    #                 dict[value_i] = 1
    #             else:
    #                 dict[value_i] += 1
    #     return dict

    # def inventario_x_consumo(self):
    #     consumo = self.inf_ingredients()
    #     print('consumo', consumo)
    #     inventory = self.inventory
    #     list_consumo = []
    #     for k, v in consumo.items():
    #         list_consumo.append((k, v))
    #     list_inventory = []
    #     for key, value in inventory[0].items():
    #         list_inventory.append((key, value))
    #     resp = []
    #     for index in list_inventory:
    #         for i in list_consumo:
    #             if index[0] == i[0]:
    #                 resp.append((index[0], index[1] - i[1]))
    #     return resp

    def get_quantities_to_buy(self):
        pedidos = {}
        list_igredientes = self.ingredients
        ingredientes = {}
        for i in self.orders:
            if i['b'] not in pedidos:
                pedidos[i['b']] = 1
            else:
                pedidos[i['b']] += 1
        for index in list_igredientes:
            for k, v in pedidos.items():
                if k == index[0]:
                    for value in list(index[1]):
                        if value not in ingredientes:
                            ingredientes[value] = v
                else:
                    for value2 in list(index[1]):
                        if value2 not in ingredientes:
                            ingredientes[value2] = 0
        return ingredientes
