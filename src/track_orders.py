from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        print(self.orders)
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        dishes = [item[1] for item in self.orders if costumer in item]
        dish_count = Counter(dishes)
        return max(dish_count, key=dish_count.get)

    def get_never_ordered_per_costumer(self, costumer):
        orders_set = set(item[1] for item in self.orders)
        set_filter = set(
              [item[1] for item in self.orders if costumer in item])
        return orders_set - set_filter

    def get_days_never_visited_per_costumer(self, costumer):
        orders_set = set(item[2] for item in self.orders)
        set_filter = set(
              [item[2] for item in self.orders if costumer in item])
        return orders_set - set_filter

    def get_busiest_day(self):
        days = [item[2] for item in self.orders]
        day_count = Counter(days)
        return max(day_count, key=day_count.get)

    def get_least_busy_day(self):
        days = [item[2] for item in self.orders]
        day_count = Counter(days)
        return min(day_count, key=day_count.get)
