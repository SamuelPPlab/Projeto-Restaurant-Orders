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
        self.orders.append({'a': costumer, 'b': order, 'c': day})
        list_comprar = []
        qtde_comprar = self.get_quantities_to_buy()
        for k, v in qtde_comprar.items():
            list_comprar.append((k, v))
        qtde_minima = self.inventory
        for k, v in qtde_minima[0].items():
            for i in list_comprar:
                if i[0] == k and i[1] < v:
                    return False

    def inf_orders(self):
        for i in self.orders:
            if i['b'] in self.ingredients_orders:
                self.ingredients_orders[i['b']] += 1
            else:
                self.ingredients_orders[i['b']] = 1

    def inf_ingredients(self):
        self.inf_orders()
        dict = {}
        ingredientes = []
        for k, v in self.ingredients_orders.items():
            for index in self.ingredients:
                if k == index[0]:
                    ingredientes.append(index[1])
        for value in ingredientes:
            for value_i in value:
                if value_i not in dict:
                    dict[value_i] = 1
                else:
                    dict[value_i] += 1
        return dict

    def consumo_de_ingredientes(self):
        pedidos = self.pedidos()
        dict = {}
        for index in self.ingredients:#prato+ingredientes
            # print(index[0]) # prato
            # print(index[1]) # lista de ingredientes
            for k, v in pedidos.items():
                if k == index[0]:
                    for i in index[1]:
                        if i not in dict:
                            dict[i] = v
                        else:
                            dict[i] += v
        return dict
        #         if index[0] == k:
        #             for i in index[1]:
        #                 if i not in dict:
        #                     dict[i] = 1
        #                 else:
        #                     dict[i] += 1
        # return dict

        # consumo = self.inf_ingredients()
        # inventory = self.inventory
        # list_consumo = []
        # for k, v in consumo.items():
        #     list_consumo.append((k, v))
        # list_inventory = []
        # for key, value in inventory[0].items():
        #     list_inventory.append((key, value))
        # resp = []
        # for index in list_inventory:
        #     for i in list_consumo:
        #         if index[0] == i[0]:
        #             resp.append((index[0], index[1]))
        # return resp
    
    def pedidos(self):
        dict = {}
        for i in self.orders:
            if i['b'] not in dict:
                dict[i['b']] = 1
            else:
                dict[i['b']] += 1
        return dict

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
                            ingredientes[value] += v
                else:
                    for value2 in list(index[1]):
                        if value2 not in ingredientes:
                            ingredientes[value2] = 0
        return ingredientes

    def get_available_dishes(self):
        print(self.pedidos())
        # for index in self.ingredients:#prato+ingredientes
        # print(index[0]) #prato
        # print(index[1]) # lista de ingredientes

        #self.inventory[0] #quantidade de ingredientes minimo
        # {'pao': 50, 'carne': 50, 'queijo': 100, 'molho': 50, 'presunto': 50, 'massa': 50, 'frango': 50}
        # for k,v in self.inventory[0].items():
        #     print(k)
        #     print(v)

        # consumo_ingredientes = self.consumo_de_ingredientes()
        # for i in consumo_ingredientes:
        #     print(i[0]) #ingrediente
        #     print(i[1]) #quantidade
            # massa
            # 50
            # frango
            # 50

        consumo_ingredientes = self.consumo_de_ingredientes()
        print('consumo de ingredientes', consumo_ingredientes)
        fingredientes = set()
        for k, v in self.inventory[0].items():
            for key, value in consumo_ingredientes.items():
                # print('ingrediente', i[0])
                # print('quantidade', i[1])
                if k == key and v == value:
                    fingredientes.add((k))
        print('fingredientes', fingredientes)

        idisponiveis = set()
        for index in self.ingredients:#prato+ingredientes
            # print(index[0]) #prato
            # print(index[1]) # lista de ingredientes
            for i in index[1]:
                if i not in fingredientes:
                    # print('sim', i)
                    # sim carne
                    # sim queijo
                    # sim queijo
                    # sim molho
                    # sim pao
                    # sim queijo
                    # sim presunto
                    idisponiveis.add((i))
        print('idisponiveis', idisponiveis)

        lista = set()
        for index in self.ingredients:#prato+ingredientes
            # print(index[0]) #prato
            # print(index[1]) # lista de ingredientes
            tamanho = len(index[1])
            count = 0
            for i in index[1]:
                if i in idisponiveis:
                    count += 1
                    if count == tamanho:
                        lista.add((index[0]))
        print('pratos disponiveis', lista)

        # conj = set()
        # for i in self.ingredients:
        #     conj.add((i[0]))
        # return conj
        return lista
