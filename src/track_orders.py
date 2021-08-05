class TrackOrders:
    orders = []

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_order_frequency_per_costumer(self, costumer, food):
        order = {}

        def filter_customer(x):
            return costumer in x

        orders_costumer = list(filter(filter_customer, self.orders))
        for client, order_client, day in orders_costumer:
            if order_client not in order:
                order[order_client] = set()
                order[order_client] = 0

            order[order_client] += 1

        return order[food]

    def search_qtd(self, list):
        count = 0
        order_more_requeted = ""
        for item, qtd in list.items():
            if qtd > count:
                count = qtd
                order_more_requeted = item
        return order_more_requeted

    def get_most_ordered_dish_per_costumer(self, costumer):
        order = {}

        def filter_customer(x):
            return costumer in x

        orders_costumer = list(filter(filter_customer, self.orders))
        for client, order_client, day in orders_costumer:
            if order_client not in order:
                order[order_client] = set()
                order[order_client] = 0

            order[order_client] += 1

        return self.search_qtd(order)

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = set()
        orders = set()

        for client, order, day in self.orders:
            all_orders.add(order)
            if client == costumer:
                orders.add(order)

        return all_orders.difference(orders)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        days = set()

        for client, order, day in self.orders:
            all_days.add(day)
            if client == costumer:
                days.add(day)

        return all_days.difference(days)

    def get_busiest_day(self):
        days = {}
        for client, order_client, day in self.orders:
            if day not in days:
                days[day] = set()
                days[day] = 0

            days[day] += 1
        return self.search_qtd(days)

    def get_least_busy_day(self):
        days = {}
        for client, order_client, day in self.orders:
            if day not in days:
                days[day] = set()
                days[day] = 0
            days[day] += 1

        order_more_requeted = list(days.keys())[0]
        count = list(days.values())[0]
        for item, qtd in days.items():
            if qtd < count:
                count = qtd
                order_more_requeted = item
        return order_more_requeted
