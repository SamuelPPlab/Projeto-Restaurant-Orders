from src import analyze_log as analyzer


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        return analyzer.most_ordered_dish_per_customer(self.orders, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return analyzer.never_ordered_per_customer(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return analyzer.days_never_visited_per_customer(self.orders, costumer)

    def get_busiest_day(self):
        day_count = _day_count(self.orders)
        return max(day_count, key=day_count.get)

    def get_least_busy_day(self):
        day_count = _day_count(self.orders)
        return min(day_count, key=day_count.get)


def _day_count(orders):
    day_count = dict()
    for order in orders:
        day = order[2]
        if day in day_count:
            day_count[day] += 1
        else:
            day_count[day] = 1
    return day_count
