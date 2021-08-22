class TrackOrders:
    def __init__(self):
        self.orders = []

    def items(self, client):
        clientOrders = []
        for order in self.orders:
            if (order['costumer'] == client):
                clientOrders.append(order['order'])
        return clientOrders

    def days(self, client):
        clientOrders = []
        for order in self.orders:
            if (order['costumer'] == client):
                clientOrders.append(order['day'])
        return clientOrders

    def get_menu(self):
        menu = []
        for order in self.orders:
            menu.append(order['order'])
        return set(menu)

    def get_days(self):
        days = []
        for order in self.orders:
            days.append(order['day'])
        return set(days)

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({
            'costumer': costumer,
            'order': order,
            'day': day,
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        clientOrders = self.items(costumer)
        return max(clientOrders, key=clientOrders.count)

    def get_never_ordered_per_costumer(self, costumer):
        menu = self.get_menu()
        clientOrders = self.items(costumer)
        return menu.symmetric_difference(clientOrders)

    def get_days_never_visited_per_costumer(self, costumer):
        days = self.get_days()
        clientOrders = self.days(costumer)
        return days.symmetric_difference(clientOrders)

    def get_busiest_day(self):
        days = []
        for order in self.orders:
            days.append(order['day'])
        return max(days, key=days.count)

    def get_least_busy_day(self):
        days = []
        for order in self.orders:
            days.append(order['day'])
        return min(days, key=days.count)
