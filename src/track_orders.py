import src.analyze_log as func


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        return func.favorite_plate(costumer, self.orders)

    def get_never_ordered_per_costumer(self, costumer):
        return func.plates_never_ordered(costumer, self.orders)

    def get_days_never_visited_per_costumer(self, costumer):
        return func.days_without_orders(costumer, self.orders)

    def get_busiest_day(self):
        days_count_order = dict()
        max_order = 0
        busiest_day = ""
        for order in self.orders:
            if order[2] in days_count_order:
                days_count_order[order[2]] += 1
            else:
                days_count_order[order[2]] = 1

            if days_count_order[order[2]] > max_order:
                max_order = days_count_order[order[2]]
                busiest_day = order[2]
        return busiest_day

    def get_least_busy_day(self):
        days_count_order = dict()
        min_order = 999
        least_busy_day = ""
        for order in self.orders:
            if order[2] in days_count_order:
                days_count_order[order[2]] += 1
            else:
                days_count_order[order[2]] = 1

            if days_count_order[order[2]] <= min_order:
                min_order = days_count_order[order[2]]
                least_busy_day = order[2]
        return least_busy_day
