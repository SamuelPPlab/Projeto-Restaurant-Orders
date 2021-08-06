from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders_food = []
        for order in self.orders:
            if order[0] == costumer:
                orders_food.append(order[1])
        return Counter(orders_food).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        days = []
        for order in self.orders:
            days.append(order[2])
        return Counter(days).most_common(1)[0][0]

    def get_least_busy_day(self):
        days = []
        for order in self.orders:
            days.append(order[2])
        return Counter(days).most_common()[-1][0]
