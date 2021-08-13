class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = {}
        result = self.orders[0][1]
        for order in self.orders:
            if order[0] == costumer:
                if order[1] not in count:
                    count[order[1]] = 1
                else:
                    count[order[1]] += 1
                if count[order[1]] > count[result]:
                    result = order[1]
        return result

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = set()
        order_by_name = set()
        for order in self.orders:
            all_orders.add(order[1])
        for order in self.orders:
            if order[0] == costumer:
                order_by_name.add(order[1])
        return all_orders.difference(order_by_name)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        day_by_name = set()
        for order in self.orders:
            all_days.add(order[2])
        for order in self.orders:
            if order[0] == costumer:
                day_by_name.add(order[2])
        return all_days.difference(day_by_name)

    def get_busiest_day(self):
        count = {}
        result = self.orders[0][2]
        for order in self.orders:
            if order[2] not in count:
                count[order[2]] = 1
            else:
                count[order[2]] += 1
            if count[order[2]] > count[result]:
                result = order[2]
        return result

    def get_least_busy_day(self):
        count = {}
        result = self.orders[0][2]
        for order in self.orders:
            if order[2] not in count:
                count[order[2]] = 1
            else:
                count[order[2]] += 1
            if count[order[2]] < count[result]:
                result = order[2]
        return result
