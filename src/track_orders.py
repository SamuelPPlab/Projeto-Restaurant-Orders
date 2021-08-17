# from collections import Counter

class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append({'a': costumer, 'b': order, 'c': day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        mais_pedido = {}
        for i in self.orders:
            if i['a'] == costumer:
                if i['b'] not in mais_pedido:
                    mais_pedido[i['b']] = 1
                else:
                    mais_pedido[i['b']] += 1
        sorted_pedidos = sorted(
                mais_pedido.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_pedidos[0][0]

    def get_dish_quantity_per_costumer(self, costumer, order):
        consumo_cliente = {}
        for i in self.orders:
            if i['a'] == costumer and i['b'] == order:
                if i['b'] not in consumo_cliente:
                    consumo_cliente[i['b']] = 1
                else:
                    consumo_cliente[i['b']] += 1
        return list(consumo_cliente.items())[0][1]

    def get_never_ordered_per_costumer(self, costumer):
        consumo = set()
        pratos = set()
        for i in self.orders:
            if i['a'] == costumer:
                consumo.add(i['b'])
            pratos.add(i['b'])
        # print('pratos', pratos)
        # print('consumo', consumo)
        return pratos - consumo

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
