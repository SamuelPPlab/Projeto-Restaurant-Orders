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
            name = item[0]
            food = item[1]
            if item[0] == name:
                if item[1] in data_client:
                    data_client[food] += 1
                else:
                    data_client[food] = 1
        return max(data_client, key=data_client.get)

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass


# consultado o seguinte PR:
# https://github.com/tryber/sd-07-restaurant-orders/pull/1/files
