from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        o_list = [order[1] for order in self.orders if order[0] == costumer]
        return (Counter(o_list).most_common(1))[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        dishes = [order[1] for order in self.orders]
        o_list = [order[1] for order in self.orders if order[0] == costumer]
        return (set(dishes)).difference(set(o_list))

    def get_days_never_visited_per_costumer(self, costumer):
        days = [order[2] for order in self.orders]
        o_list = [order[2] for order in self.orders if order[0] == costumer]
        return (set(days)).difference(set(o_list))

    def get_busiest_day(self):
        days = [order[2] for order in self.orders]
        return (Counter(days).most_common(1))[0][0]

    def get_least_busy_day(self):
        days = [order[2] for order in self.orders]
        return (Counter(days).most_common())[-1][0]
