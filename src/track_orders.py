class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        dish_count = {}
        for order in self.orders:
            if order[0] == costumer:
                if order[1] in dish_count:
                    dish_count[order[1]] += 1
                else:
                    dish_count[order[1]] = 1
        return max(dish_count, key=dish_count.get)

    def get_never_ordered_per_costumer(self, costumer):
        client_order = set()
        all_orders = set()
        for order in self.orders:
            all_orders.add(order[1])
            if order[0] == costumer:
                client_order.add(order[1])
        return all_orders - client_order

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        day_count = {}
        for order in self.orders:
            if order[2] in day_count:
                day_count[order[2]] += 1
            else:
                day_count[order[2]] = 1
        return max(day_count, key=day_count.get)

    def get_least_busy_day(self):
        day_count = {}
        for order in self.orders:
            if order[2] in day_count:
                day_count[order[2]] += 1
            else:
                day_count[order[2]] = 1
        return min(day_count, key=day_count.get)
