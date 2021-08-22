from collections import Counter


class TrackOrders:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def add_new_order(self, costumer, order, day):
        self.array.append({'client': costumer, 'order': order, 'day': day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = []
        for element in self.array:
            if element['client'] == costumer:
                orders.append(element['order'])
        counter = Counter(orders)
        return list(counter.keys())[0]

    def get_never_ordered_per_costumer(self, costumer):
        orders_already_ordered = set()
        all_orders = set()
        for element in self.array:
            all_orders.add(element['order'])
            if element['client'] == costumer:
                orders_already_ordered.add(element['order'])
        return all_orders.difference(orders_already_ordered)

    def get_dish_quantity_per_costumer(self, costumer, order):
        c = 0
        for element in self.array:
            if element['client'] == costumer and element['order'] == order:
                c = c + 1
        return c

    def get_days_never_visited_per_costumer(self, costumer):
        days_already_done = set()
        all_days = set()
        for element in self.array:
            all_days.add(element['day'])
            if element['client'] == costumer:
                days_already_done.add(element['day'])
        return all_days.difference(days_already_done)

    def get_busiest_day(self):
        days = []
        for element in self.array:
            days.append(element['day'])
        counter = Counter(days)
        return list(counter.keys())[0]

    def get_least_busy_day(self):
        days = []
        for element in self.array:
            days.append(element['day'])
        counter = Counter(days)
        return list(counter.keys())[-1]
