from collections import Counter


class TrackOrders:
    def __init__(self):
        self.list_orders = list()

    def __len__(self):
        return len(self.list_orders)

    def add_new_order(self, costumer, order, day):
        new_order = [costumer, order, day]
        self.list_orders.append(new_order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        lista_pedido_cliente = [
            order[1] for order in self.list_orders if order[0] == costumer
        ]
        prato_mais_pedido = Counter(lista_pedido_cliente).most_common(1)[0][0]
        return prato_mais_pedido

    def get_never_ordered_per_costumer(self, costumer):
        listar_pedidos = set([order[1] for order in self.list_orders])

        lista_pedido_cliente = set(
            [order[1] for order in self.list_orders if order[0] == costumer]
        )

        return listar_pedidos.difference(lista_pedido_cliente)

    def get_dish_quantity_per_costumer(self, costumer, order):
        lista_pedido_cliente = [
            prato[1]
            for prato in self.list_orders
            if prato[0] == costumer and prato[1] == order
        ]

        return len(lista_pedido_cliente) if lista_pedido_cliente else 0

    def get_days_never_visited_per_costumer(self, costumer):
        todos_os_dias = set([order[2] for order in self.list_orders])

        dias_do_cliente = set(
            [order[2] for order in self.list_orders if order[0] == costumer]
        )

        return todos_os_dias.difference(dias_do_cliente)

    def get_busiest_day(self):
        todos_os_dias = [order[2] for order in self.list_orders]
        dias_mais_repetidos = Counter(todos_os_dias).most_common(1)[0][0]
        return dias_mais_repetidos

    def get_least_busy_day(self):
        todos_os_dias = [order[2] for order in self.list_orders]
        dias_menos_repetidos = Counter(todos_os_dias).most_common()[-1][0]
        return dias_menos_repetidos
