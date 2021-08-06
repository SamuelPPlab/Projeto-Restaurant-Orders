class Clients_data:
    def __init__(self, client, data):
        self.client = client
        self.orders = [row['order'] for row in data if client in row['client']]
        self.week_days = [
            row['week_day'] for row in data if client in row['client']
        ]


class TrackOrders:
    def __init__(self):
        self.orders = []


    def __len__(self):
        return len(self.orders)


    def add_new_order(self, costumer, order, day):
        self.orders.append({
            'client': costumer,
            'order': order,
            'week_day': day
        })


    def get_most_ordered_dish_per_costumer(self, costumer):
        client = Clients_data(costumer, self.orders)

        aux_count = {}
        most_ordered = client.orders[0]

        for client_order in client.orders:
            if client_order not in aux_count:
                aux_count[client_order] = 1
            else:
                aux_count[client_order] += 1
  
            if aux_count[client_order] > aux_count[most_ordered]:
                most_ordered = client_order

        return most_ordered


    def get_never_ordered_per_costumer(self, costumer):
        client = Clients_data(costumer, self.orders)
        all_orders = [row['order'] for row in self.orders]
        never_ordered = set(all_orders) - set(client.orders)
        return never_ordered


    def get_days_never_visited_per_costumer(self, costumer):
        client = Clients_data(costumer, self.orders)

        all_week_days = [row['week_day'] for row in self.orders]
        days_never_visited = set(all_week_days) - set(client.week_days)
        return days_never_visited


    def get_busiest_day(self):
        pass


    def get_least_busy_day(self):
        pass
