from collections import Counter


class TrackOrders:
    def __init__(self):
        self.products_orded = list()

    def __len__(self):
        return len(self.products_orded)

    def add_new_order(self, costumer, order, day):
        return self.products_orded.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = [
            order[1] for order in self.products_orded if order[0] == costumer
        ]
        most_ordered_dish = Counter(orders).most_common(1)[0][0]
        return most_ordered_dish

    def get_never_ordered_per_costumer(self, costumer):
        products = set([order[1] for order in self.products_orded])
        never_ordered = set(
            [order[1] for order in self.products_orded if order[0] == costumer]
        )

        return products.difference(never_ordered)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set(order[2] for order in self.products_orded)
        visited_days_by_client = set(
            order[2] for order in self.products_orded if order[0] == costumer
        )
        days_not_visited = days.difference(visited_days_by_client)
        return days_not_visited

    def get_busiest_day(self):
        list_all_days = [order[2] for order in self.products_orded]
        most_repeated_day = Counter(list_all_days).most_common(1)[0][0]
        return most_repeated_day

    def get_least_busy_day(self):
        list_all_days = [order[2] for order in self.products_orded]
        less_repeated_day = Counter(list_all_days).most_common()[-1][0]
        return less_repeated_day
