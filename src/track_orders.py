from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        dish_list = []

        for item in self.orders:
            if item[0] == costumer:
                dish_list.append(item[1])

        most_eaten_dish, _ = Counter(dish_list).most_common()[0]
        return most_eaten_dish

    def get_never_ordered_per_costumer(self, costumer):
        dishes = set()
        ordered_dish = set()

        for item in self.orders:
            dishes.add(item[1])
            if item[0] == costumer:
                ordered_dish.add(item[1])

        return dishes.difference(ordered_dish)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        visit_days = set()

        for item in self.orders:
            days.add(item[2])
            if item[0] == costumer:
                visit_days.add(item[2])

        return days.difference(visit_days)

    def get_busiest_day(self):
        days = []
        for item in self.orders:
            days.append(item[2])

        most_visit_day, _ = Counter(days).most_common()[0]

        return most_visit_day

    def get_least_busy_day(self):
        days = []
        for item in self.orders:
            days.append(item[2])

        least_visit_day, _ = Counter(days).most_common()[-1]

        return least_visit_day
