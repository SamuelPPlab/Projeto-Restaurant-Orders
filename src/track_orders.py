class TrackOrders:
    def __init__(self):
        self.infos = []

    def __len__(self):
        return len(self.infos)

    def add_new_order(self, costumer, order, day):
        self.infos.append({"nome": costumer, "pedido": order, "dia": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        info_pedidos = {}

        for pedido in self.infos:
            if pedido["nome"] == costumer:
                if pedido["pedido"] in info_pedidos:
                    info_pedidos[pedido["pedido"]] += 1
                else:
                    info_pedidos[pedido["pedido"]] = 1

        return max(info_pedidos, key=info_pedidos.get)

    def get_never_ordered_per_costumer(self, costumer):
        pratos = set()
        pratosDoCliente = set()

        for pedido in self.infos:
            pratos.add(pedido["pedido"])
            if pedido["nome"] == costumer:
                pratosDoCliente.add(pedido["pedido"])

        return pratos.difference(pratosDoCliente)

    def get_days_never_visited_per_costumer(self, costumer):
        dias = set()
        diasDoCliente = set()

        for pedido in self.infos:
            dias.add(pedido["dia"])
            if pedido["nome"] == costumer:
                diasDoCliente.add(pedido["dia"])

        return dias.difference(diasDoCliente)

    def get_busiest_day(self):
        dias = {}

        for pedido in self.infos:
            if pedido["dia"] in dias:
                dias[pedido["dia"]] += 1
            else:
                dias[pedido["dia"]] = 1

        return max(dias, key=dias.get)

    def get_least_busy_day(self):
        dias = {}

        for pedido in self.infos:
            if pedido["dia"] in dias:
                dias[pedido["dia"]] += 1
            else:
                dias[pedido["dia"]] = 1

        return min(dias, key=dias.get)
