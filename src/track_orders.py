from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumerOrders = [
            order[1] for order in self.orders if order[0] == costumer
        ]
        return Counter(costumerOrders).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        allOrders = {order[1] for order in self.orders}
        costumerOrders = {
            order[1] for order in self.orders if order[0] == costumer
        }
        return allOrders.difference(costumerOrders)

    def get_days_never_visited_per_costumer(self, costumer):
        allDays = {order[2] for order in self.orders}
        costumerDays = {
            order[2] for order in self.orders if order[0] == costumer
        }
        return allDays.difference(costumerDays)

    def get_busiest_day(self):
        allDays = [order[2] for order in self.orders]
        return Counter(allDays).most_common(1)[0][0]

    def get_least_busy_day(self):
        allDays = [order[2] for order in self.orders]
        return Counter(allDays).most_common()[-1][0]
