from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        ordered_meals = []
        for order in self.orders:
            if order[0] == costumer:
                ordered_meals.append(order[1])
        return Counter(ordered_meals).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        meals_list = set()
        client_ordered_meals = set()
        for order in self.orders:
            meals_list.add(order[1])
        for order in self.orders:
            if order[0] == costumer:
                client_ordered_meals.add(order[1])
        return meals_list.difference(client_ordered_meals)

    def get_days_never_visited_per_costumer(self, costumer):
        week_days = set()
        client_ordered_days = set()
        for order in self.orders:
            week_days.add(order[2])
        for order in self.orders:
            if order[0] == costumer:
                client_ordered_days.add(order[2])
        return week_days.difference(client_ordered_days)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
