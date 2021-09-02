from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders_list = []

        for order in self.orders:
            if order[0] == costumer:
                orders_list.append(order[1])

        return Counter(orders_list).most_common()[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        all_foods = set(order[1] for order in self.orders)

        foods_ordered = set(
            order[1] for order in self.orders
            if order[0] == costumer
        )

        return all_foods.difference(foods_ordered)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set(order[2] for order in self.orders)

        days_visited = set(
            order[2] for order in self.orders
            if order[0] == costumer
        )

        return days.difference(days_visited)

    def get_busiest_day(self):
        days = [
            order[2] for order in self.orders
        ]

        return Counter(days).most_common()[0][0]

    def get_least_busy_day(self):
        days = [
            order[2] for order in self.orders
        ]

        return Counter(days).most_common()[-1][0]
