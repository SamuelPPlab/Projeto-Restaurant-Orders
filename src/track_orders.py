class TrackOrders:
    def __init__(self):
        self.orders = []
        self.orders_by_client = {}
        self.orders_by_day = {}
        self.days_with_orders_by_client = {}
        self.menu = set()
        self.days_worked = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append(
            {"client_name": costumer, "order": order, "day_week": day})
        if costumer not in self.orders_by_client:
            self.orders_by_client[costumer] = [order]
            self.days_with_orders_by_client[costumer] = [day]
        else:
            self.orders_by_client[costumer].append(order)
            self.days_with_orders_by_client[costumer].append(day)
        if order not in self.menu:
            self.menu.add(order)
        if day not in self.days_worked:
            self.days_worked.add(day)
        if day not in self.orders_by_day:
            self.orders_by_day[day] = [day]
        else:
            self.orders_by_day[day].append(day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        order_count = {}
        most_frequent = self.orders_by_client[costumer][0]

        for order in self.orders_by_client[costumer]:
            if order not in order_count:
                order_count[order] = 1
            else:
                order_count[order] += 1
            if order_count[order] > order_count[most_frequent]:
                most_frequent = order
        return most_frequent

    def get_never_ordered_per_costumer(self, costumer):
        orders = set(self.orders_by_client[costumer])
        return self.menu.difference(orders)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set(self.days_with_orders_by_client[costumer])
        return self.days_worked.difference(days)

    def get_busiest_day(self):
        count = 0
        for key, value in self.orders_by_day.items():
            if len(value) > count:
                count = len(value)
                busiest = key
        return busiest

    def get_least_busy_day(self):
        count = 1000
        for key, value in self.orders_by_day.items():
            if len(value) < count:
                count = len(value)
                least_busy = key
        return least_busy
