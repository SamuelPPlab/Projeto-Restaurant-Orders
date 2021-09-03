from src.analyze_log import get_favorite_order, get_order_quantity
from src.analyze_log import get_never_visited_days, get_never_ordered_items

# customer => cliente
# costumer => costureiro/criador de fantasias


class TrackOrders:
    path = 'data/orders_1.csv'

    def __init__(self) -> None:
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, customer):
        return get_favorite_order(self.orders, customer)

    def get_dish_quantity_per_costumer(self, customer, dish):
        return get_order_quantity(self.orders, customer, dish)

    def get_never_ordered_per_costumer(self, customer):
        return get_never_ordered_items(self.orders, customer)

    def get_days_never_visited_per_costumer(self, customer):
        return get_never_visited_days(self.orders, customer)

    def count_orders_per_day(self):
        days = {}
        for order in self.orders:
            if order[2] not in days:
                days[order[2]] = 1
            else:
                days[order[2]] += 1

        return days

    def get_busiest_day(self):
        days = self.count_orders_per_day()
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = self.count_orders_per_day()
        return min(days, key=days.get)
