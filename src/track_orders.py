from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        lista = []
        for pedido in self.orders:
            if pedido[0] == costumer:
                lista.append(pedido[1])
        resultado = Counter(lista)
        return resultado.most_common()[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        todos_pedidos = set()
        pedidos_cliente = set()
        for pedido in self.orders:
            todos_pedidos.add(pedido[1])
            if pedido[0] == costumer:
                pedidos_cliente.add(pedido[1])
        return todos_pedidos.difference(pedidos_cliente)

    def get_days_never_visited_per_costumer(self, costumer):
        dias = set()
        dias_com_pedidos = set()
        for pedido in self.orders:
            dias.add(pedido[2])
            if pedido[0] == costumer:
                dias_com_pedidos.add(pedido[2])
        return dias.difference(dias_com_pedidos)

    def get_busiest_day(self):
        lista = []
        for pedido in self.orders:
            lista.append(pedido[2])
        resultado = Counter(lista)
        return resultado.most_common()[0][0]

    def get_least_busy_day(self):
        lista = []
        for pedido in self.orders:
            lista.append(pedido[2])
        resultado = Counter(lista)
        return resultado.most_common()[-1][0]
