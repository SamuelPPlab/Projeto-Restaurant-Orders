from collections import Counter


class TrackOrders:
    def __init__(self):
        self.semana = set()
        self.produtos = set()
        self.pedidos = []

    def __len__(self):
        return len(self.pedidos)

    def add_new_order(self, costumer, order, day):
        self.produtos.add(order)
        self.semana.add(day)
        self.pedidos.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        all_pedido = []
        for pedido in self.pedidos:
            if pedido[0] == costumer:
                all_pedido.append(pedido[1])
        return Counter(all_pedido).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        produto = set(self.produtos)
        for pedido in self.pedidos:
            if(pedido[0] == costumer):
                produto.discard(pedido[1])
        return produto

    def get_days_never_visited_per_costumer(self, costumer):
        dias = set(self.semana)
        for pedido in self.pedidos:
            if(pedido[0] == costumer):
                dias.discard(pedido[2])
        return dias

    def get_busiest_day(self):
        semana = []
        for pedido in self.pedidos:
            semana.append(pedido[2])
        return Counter(semana).most_common(1)[0][0]

    def get_least_busy_day(self):
        semana = []
        for pedido in self.pedidos:
            semana.append(pedido[2])
        return Counter(semana).most_common()[-1][0]
