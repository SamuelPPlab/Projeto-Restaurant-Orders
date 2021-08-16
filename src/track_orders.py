from collections import Counter


class TrackOrders:
    def __init__(self):
        self.pedidos = []

    def __len__(self):
        return len(self.pedidos)

    def add_new_order(self, costumer, order, day):
        return self.pedidos.append([costumer, order, day])

# Será validado se, ao executar get_most_ordered_dish_per_costumer,
# o método retorna o prato mais pedido.
    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_list = []
        for pedido in self.pedidos:
            costumer_list.append(pedido[1])

        return Counter(costumer_list).most_common(1)[0][0]

# Será validado se, ao executar get_never_ordered_per_costumer,
# o método retorna o pedido que o cliente nunca fez.
    def get_never_ordered_per_costumer(self, costumer):
        # referencia Tiago Esdras
        total_pedidos = set()

        for pedido in self.pedidos:
            total_pedidos.add(pedido[1])

        total_clientes = set()
        for pedido in self.pedidos:
            if pedido[0] == costumer:
                total_clientes.add(pedido[1])

        return total_pedidos.difference(total_clientes)

# Será validado se, ao executar get_days_never_visited_per_costumer,
#  o método retorna o dias que o cliente nunca visitou.
    def get_days_never_visited_per_costumer(self, costumer):
        total_dias = set()
        for pedido in self.pedidos:
            total_dias.add(pedido[2])

        total_dias_clientes = set()
        for pedido in self.pedidos:
            if pedido[0] == costumer:
                total_dias_clientes.add(pedido[2])

        return total_dias.difference(total_dias_clientes)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
