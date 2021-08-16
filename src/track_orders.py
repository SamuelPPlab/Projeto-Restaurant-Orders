import collections


class TrackOrders:
    def __len__(self):
        # pass
        return len(self.orders)

    def __init__(self):
        self.orders = []

    def add_new_order(self, costumer, order, day):
        # pass
        return self.orders.append({"a": costumer, "b": order, "c": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        # pass
        order = []
        for item in self.orders:
            if item["a"] == costumer:
                order.append(item["b"])
        return collections.Counter(order).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        # pass
        ordered = set()
        never_ordered = set()
        for item in self.orders:
            if item["a"] == costumer:
                ordered.add(item["b"])
            never_ordered.add(item["b"])
        return never_ordered.difference(ordered)

    def get_days_never_visited_per_costumer(self, costumer):
        # pass
        visited = set()
        never_visited = set()

        for item in self.orders:
            if item["a"] == costumer:
                visited.add(item["c"])
            never_visited.add(item["c"])
        return never_visited.difference(visited)

    def get_busiest_day(self):
        # pass
        busiest_day = []
        for item in self.orders:
            busiest_day.append(item["c"])
        return collections.Counter(busiest_day).most_common(1)[0][0]

    def get_least_busy_day(self):
        # pass
        least_busy_day = []
        for item in self.orders:
            least_busy_day.append(item["c"])
        return collections.Counter(least_busy_day).most_common()[-1][0]
