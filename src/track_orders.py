from analyze_log import key_selector_counter, key_selector_set


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.data = []
    
    def __len__(self):
        pass

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

    def get_most_ordered_dish_per_costumer(self, costumer):
        client_orders = self.client_fetcher(costumer)
        counted_orders = list(key_selector_counter(client_orders, 'pedido').items())
        most_common_order = ''
        count_holder = 0
        for order in counted_orders:
            if order[1] > count_holder:
                count_holder = order[1]
                most_common_order = order[0]
        return most_common_order


    def get_dish_quantity_per_costumer(self, costumer, order):
        client_orders = self.client_fetcher(costumer)

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
    
    def get_days_never_visited_per_costumer(self, customer):
        pass
