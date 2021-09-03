from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_ordered = []
        for order in self.orders:
            if order[0] == costumer:
                most_ordered.append(order[1])
        return Counter(most_ordered).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        foods = set(food[1] for food in self.orders)
        foods_orderes_by_client = set(
            item[1] for item in self.orders if item[0] == costumer
        )

        return foods - foods_orderes_by_client

    def get_days_never_visited_per_costumer(self, costumer):
        days = set(day[2] for day in self.orders)
        days_visited = set(
            item[2] for item in self.orders if item[0] == costumer
        )

        return days - days_visited

    def get_busiest_day(self):
        moviment_days = [day[2] for day in self.orders]
        return Counter(moviment_days).most_common(1)[0][0]

    def get_least_busy_day(self):
        moviment_days = [day[2] for day in self.orders]
        return Counter(moviment_days).most_common()[-1][0]
