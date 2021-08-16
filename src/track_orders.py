from collections import Counter


def frequency_days(orders):
    day_counter = dict()
    for order in orders:
        day = order[2]
        if day in day_counter:
            day_counter[day] += 1
        else:
            day_counter[day] = 1
    return day_counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        wish_list = [
            order[1] for order in self.orders if order[0] == costumer
        ]
        most_ordered_dish = Counter(wish_list).most_common(1)[0][0]
        return most_ordered_dish

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        days_count = frequency_days(self.orders)
        return max(days_count, key=days_count.get)

    def get_least_busy_day(self):
        day_count = frequency_days(self.orders)
        return min(day_count, key=day_count.get)
