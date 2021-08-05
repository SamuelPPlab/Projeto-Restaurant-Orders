from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        filter = []
        for item in self.orders:
            if item[0] == costumer:
                filter.append(item[1])
        result = Counter(filter)
        return result.most_common()[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        orderSet = set()
        customerOrderSet = set()
        for item in self.orders:
            orderSet.add(item[1])
            if item[0] == costumer:
                customerOrderSet.add(item[1])
        return orderSet.difference(customerOrderSet)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        costumerDays = set()
        for item in self.orders:
            days.add(item[2])
            if item[0] == costumer:
                costumerDays.add(item[2])
        return days.difference(costumerDays)

    def get_busiest_day(self):
        filter = []
        for item in self.orders:
            filter.append(item[2])
        result = Counter(filter)
        return result.most_common()[0][0]

    def get_least_busy_day(self):
        filter = []
        for item in self.orders:
            filter.append(item[2])
        result = Counter(filter)
        return result.most_common()[-1][0]
