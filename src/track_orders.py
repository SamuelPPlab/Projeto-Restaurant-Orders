from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_orders = [
            order[1] for order in self.orders if order[0] == costumer
        ]
        return Counter(costumer_orders).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = {order[1] for order in self.orders}
        costumer_orders = {
            order[1] for order in self.orders if order[0] == costumer
        }
        return all_orders.difference(costumer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = {order[2] for order in self.orders}
        costumer_days = {
            order[2] for order in self.orders if order[0] == costumer
        }
        return all_days.difference(costumer_days)

    def get_busiest_day(self):
        all_days = [order[2] for order in self.orders]
        return Counter(all_days).most_common(1)[0][0]

    def get_least_busy_day(self):
        all_days = [order[2] for order in self.orders]
        return Counter(all_days).most_common()[-1][0]
