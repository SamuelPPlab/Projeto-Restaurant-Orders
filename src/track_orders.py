class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.data = []

    def __len__(self):
        return self.data.__len__()

    def add_new_order(self, costumer, order, day):
        entry = {'cliente': costumer, 'pedido': order, 'dia': day}
        self.data.append(entry)

    def client_fetcher(self, cliente):
        pedidos_do_cliente = []
        for item in self.data:
            if item['cliente'] == cliente:
                pedidos_do_cliente.append(item)
        return pedidos_do_cliente

    def key_selector_counter(self, data_set, key):
        frequencia = {}
        for item in data_set:
            if item[key] not in frequencia:
                frequencia[item[key]] = 1
            else:
                frequencia[item[key]] += 1
        return frequencia

    def key_selector_set(self, data_set, key):
        frequencia = {}
        for item in data_set:
            if item[key] not in frequencia:
                frequencia[item[key]] = True
        return frequencia.keys()

    def largest_or_smallest_key_selector(self, data, largest=True):
        selected_item = ''
        count_holder = data[0][1]
        for order in data:
            if order[1] >= count_holder and largest:
                count_holder = order[1]
                selected_item = order[0]
            if order[1] <= count_holder and largest is False:
                count_holder = order[1]
                selected_item = order[0]
        return selected_item

    def get_dish_quantity_per_costumer(self, costumer, order):
        client = self.client_fetcher(costumer)
        orders = self.key_selector_counter(client, 'pedido')
        return orders[order]

    def get_never_ordered_per_costumer(self, costumer):
        client_orders = self.client_fetcher(costumer)
        menu = set(self.key_selector_set(self.data, 'pedido'))
        client = set(self.key_selector_set(client_orders, 'pedido'))
        return menu.difference(client)

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = self.client_fetcher(costumer)
        orders = list(self.key_selector_counter(orders, 'pedido').items())
        return self.largest_or_smallest_key_selector(orders)

    def get_busiest_day(self):
        weekday = list(self.key_selector_counter(self.data, 'dia').items())
        return self.largest_or_smallest_key_selector(weekday)

    def get_least_busy_day(self):
        weekday = list(self.key_selector_counter(self.data, 'dia').items())
        return self.largest_or_smallest_key_selector(weekday, False)

    def get_days_never_visited_per_costumer(self, customer):
        pedidos_do_cliente = self.client_fetcher(customer)
        cliente_foi = set(self.key_selector_set(pedidos_do_cliente, 'dia'))
        dias_da_semana = set(self.key_selector_set(self.data, 'dia'))
        return dias_da_semana.difference(cliente_foi)
