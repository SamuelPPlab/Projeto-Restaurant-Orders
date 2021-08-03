from collections import Counter
from statistics import mode


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({
            'costumer': costumer, 'order': order, 'day': day
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        return mode(
            order['order'] for order in self.orders
            if order['costumer'] == costumer
        )

    def get_never_ordered_per_costumer(self, costumer):
        dishes = set([order['order'] for order in self.orders])
        customer_dishes = set([
            order['order']
            for order in self.orders
            if order['costumer'] == costumer
        ])

        return dishes.difference(customer_dishes)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set([order['day'] for order in self.orders])
        customer_visited_days = set([
            order['day']
            for order in self.orders
            if order['costumer'] == costumer
        ])
        return days.difference(customer_visited_days)

    def get_busiest_day(self):
        return mode(
            order['day'] for order in self.orders
        )

    def get_least_busy_day(self):
        count_costumer_order = Counter(
            order['day'] for order in self.orders
        )

        return min(count_costumer_order, key=count_costumer_order.get)
