from statistics import mode

# mode é uma função que retorna o valor mais presente em um conjunto de valores.


class TrackOrders:
    def __init__(self):
        self.pedidos = []

    def __len__(self):
        return len(self.pedidos)

    def add_new_order(self, costumer, order, day):
        self.pedidos.append({"nome": costumer, "pedido": order, "dia": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        todosPratos = {}

        for pedido in self.pedidos:
            if pedido["nome"] == costumer and pedido["pedido"] in todosPratos:
                todosPratos[pedido["pedido"]] += 1
            elif pedido["nome"] == costumer:
                todosPratos[pedido["pedido"]] = 1

        return max(todosPratos, key=todosPratos.get)

    def get_never_ordered_per_costumer(self, costumer):
        todosOsPratos = set()

        for pedido in self.pedidos:
            todosOsPratos.add(pedido["pedido"])

        pratosDoCliente = set()

        for pedido in self.pedidos:
            if pedido["nome"] == costumer:
                pratosDoCliente.add(pedido["pedido"])

        return todosOsPratos.difference(pratosDoCliente)

    def get_days_never_visited_per_costumer(self, costumer):
        todosDias = set()

        for pedido in self.pedidos:
            todosDias.add(pedido["dia"])

        diasQueClienteFrequentou = set()

        for pedido in self.pedidos:
            if pedido["nome"] == costumer:
                diasQueClienteFrequentou.add(pedido["dia"])

        return todosDias.difference(diasQueClienteFrequentou)

    def get_busiest_day(self):
        todosDias = {}

        for pedido in self.pedidos:
            if pedido["dia"] in todosDias:
                todosDias[pedido["dia"]] += 1
            else:
                todosDias[pedido["dia"]] = 1

        return max(todosDias, key=todosDias.get)

    def get_least_busy_day(self):
        todosDias = {}

        for pedido in self.pedidos:
            if pedido["dia"] in todosDias:
                todosDias[pedido["dia"]] += 1
            else:
                todosDias[pedido["dia"]] = 1

        return min(todosDias, key=todosDias.get)
