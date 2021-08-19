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

    def alimenta_dic_c_ingredientes(self, index, v, dict):
        for i in index[1]:
            if i not in dict:
                dict[i] = v
            else:
                dict[i] += v

    def consumo_de_ingredientes(self):
        dict = {}
        for index in self.ingredients:
            for k, v in self.pedidos().items():
                if k == index[0]:
                    self.alimenta_dic_c_ingredientes(index, v, dict)
        return dict

    def pedidos(self):
        dict = {}
        for i in self.orders:
            if i['b'] not in dict:
                dict[i['b']] = 1
            else:
                dict[i['b']] += 1
        return dict

    def inserir_0_nao_consumo(self, index, ingredientes):
        for value2 in list(index[1]):
            if value2 not in ingredientes:
                ingredientes[value2] = 0

    def get_quantities_to_buy(self):
        ingredientes = {}
        for index in self.ingredients:
            for k, v in self.pedidos().items():
                if k == index[0]:
                    self.alimenta_dic_c_ingredientes(index, v, ingredientes)
                else:
                    self.inserir_0_nao_consumo(index, ingredientes)
        return ingredientes

    def ingredientes_faltando(self):
        consumo_ingredientes = self.consumo_de_ingredientes()
        fingredientes = set()
        for k, v in self.inventory[0].items():
            for key, value in consumo_ingredientes.items():
                if k == key and v == value:
                    fingredientes.add((k))
        return fingredientes

    def ingredientes_disponiveis(self):
        idisponiveis = set()
        for index in self.ingredients:
            for i in index[1]:
                if i not in self.ingredientes_faltando():
                    idisponiveis.add((i))
        return idisponiveis

    def get_available_dishes(self):
        lista = set()
        for index in self.ingredients:
            tamanho = len(index[1])
            count = 0
            for i in index[1]:
                if i in self.ingredientes_disponiveis():
                    count += 1
                    if count == tamanho:
                        lista.add((index[0]))
        print('pratos disponiveis', lista)
        return lista
