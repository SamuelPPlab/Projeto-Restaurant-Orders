from typing import Counter


class TrackOrders:
    def __init__(self):
        self.orders = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.add((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        dish_ordered = self.costumer_meals(costumer)
        count = 0
        most_ordered = ''

        for dish in dish_ordered:
            if dish_ordered.count(dish) > count:
                count = dish_ordered.count(dish)
                most_ordered = dish
        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        order = set()
        dishes = set()

        for product in self.orders:
            dishes.add[product["order"]]
            if product["costumer"] == costumer:
                order.add(product["order"])
        return dishes.difference(order)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        client_days = set()

        for day in self.orders:
            all_days.add(day[2])
        for client in self.orders:
            if client[0] == costumer:
                client_days.add(client[2])
        return all_days.difference(client_days)

    def get_busiest_day(self):
        working_days = []
        for day in self.orders:
            working_days.append(day[2])
        busiest_day = Counter(working_days).most_common(1)[0][0]
        return busiest_day

    def get_least_busy_day(self):
        working_days = []
        for day in self.orders:
            working_days.append(day[2])
        emptiest_day = Counter(working_days).most_common()[-1][0]
        return emptiest_day
