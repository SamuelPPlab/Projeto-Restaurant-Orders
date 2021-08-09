class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        data_client = {}
        for item in self.orders:
            food = item[1]
            if item[0] == costumer:
                if item[1] in data_client:
                    data_client[food] += 1
                else:
                    data_client[food] = 1
        return max(data_client, key=data_client.get)

    def get_never_ordered_per_costumer(self, costumer):
        client_orders = set()
        carte = set()
        for item in self.orders:
            name = item[0]
            food = item[1]
            carte.add(food)
            if name == costumer:
                client_orders.add(food)
        return carte - client_orders

    def get_days_never_visited_per_costumer(self, costumer):
        client_orders = set()
        open_days = set()
        for item in self.orders:
            name = item[0]
            day = item[2]
            open_days.add(day)
            if name == costumer:
                client_orders.add(day)
        return open_days - client_orders

    def get_busiest_day(self):
        days = {}
        for item in self.orders:
            day = item[2]
            if day in days:
                days[day] += 1
            else:
                days[day] = 1
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = {}
        for item in self.orders:
            day = item[2]
            if day in days:
                days[day] += 1
            else:
                days[day] = 1
        return min(days, key=days.get)


# consultado o seguinte PR:
# https://github.com/tryber/sd-07-restaurant-orders/pull/1/files
