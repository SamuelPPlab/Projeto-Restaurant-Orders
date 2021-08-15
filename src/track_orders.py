class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = {}
        for order in self.orders:
            if order['costumer'] == costumer:
                if order['order'] in orders:
                    orders[order['order']] += 1
                else:
                    orders[order['order']] = 1
        return max(orders, key=orders.get)

    def get_never_ordered_per_costumer(self, costumer):
        all_dishes = set()
        client_dishes = set()
        for order in self.orders:
            all_dishes.add(order['order'])
            if order['costumer'] == costumer:
                client_dishes.add(order['order'])
        return all_dishes.difference(client_dishes)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        client_days = set()
        for order in self.orders:
            all_days.add(order['day'])
            if order['costumer'] == costumer:
                client_days.add(order['day'])
        return all_days.difference(client_days)

    def get_busiest_day(self):
        daily_frequency = {}
        for order in self.orders:
            if order['day'] in daily_frequency:
                daily_frequency[order['day']] += 1
            else:
                daily_frequency[order['day']] = 1
        return max(daily_frequency, key=daily_frequency.get)

    def get_least_busy_day(self):
        daily_frequency = {}
        for order in self.orders:
            if order['day'] in daily_frequency:
                daily_frequency[order['day']] += 1
            else:
                daily_frequency[order['day']] = 1
        return min(daily_frequency, key=daily_frequency.get)
