from collections import Counter


class TrackOrders:
    def __init__(self):
        self.products_ordered = []

    def __len__(self):
        return len(self.products_ordered)

    def add_new_order(self, costumer, order, day):
        return self.products_ordered.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = list(
            item[1] for item in self.products_ordered
            if item[0] == costumer
        )
        most_ordered = Counter(orders).most_common()[0][0]
        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        products = set(item[1] for item in self.products_ordered)
        products_by_client = set(
            item[1] for item in self.products_ordered
            if item[0] == costumer
        )
        unordered_products = products.difference(products_by_client)
        return unordered_products

    def get_days_never_visited_per_costumer(self, costumer):
        days = set(item[2] for item in self.products_ordered)
        visited_days_by_client = set(
            item[2] for item in self.products_ordered
            if item[0] == costumer
        )
        days_not_visited = days.difference(visited_days_by_client)
        return days_not_visited

    def get_busiest_day(self):
        days = list(
            item[2] for item in self.products_ordered
        )
        busiest_day = Counter(days).most_common()[0][0]
        return busiest_day

    def get_least_busy_day(self):
        days = list(
            item[2] for item in self.products_ordered
        )
        least_busiest_day = Counter(days).most_common()[-1][0]
        return least_busiest_day
