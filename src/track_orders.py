
from collections import Counter

class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"name": costumer, "order": order, "day": day})

    def get_customer_orders(self, customer_name):
        customer_orders = []
        for order in self.orders:
            if order["name"] == customer_name:
                customer_orders.append(order["order"])
        counter = Counter(customer_orders)
        return counter

    def get_most_ordered_dish_per_costumer(self, costumer):
        counter = self.get_customer_orders(costumer)
        most_frequent = counter.most_common(1)[0][0]
        print(most_frequent)
        return most_frequent

    def get_dish_type(self):
        dishes_type = {order["order"] for order in self.orders}
        return dishes_type

    def get_never_ordered_per_costumer(self, costumer):
        dishes_type = self.get_dish_type()
        customer_orders = self.get_customer_orders(costumer)
        never_ordered = dishes_type.symmetric_difference(customer_orders)
        return never_ordered

    def get_visited_day(self):
        days = {order["day"] for order in self.orders}
        return days

    def get_customer_day_visited(self, customer_name):
        days = {
            order["day"]
            for order in self.orders
            if order["name"] == customer_name
        }
        return days

    def get_days_never_visited_per_costumer(self, costumer):
        days = self.get_visited_day()
        customer_orders = self.get_customer_day_visited(costumer)
        never_visited = days.symmetric_difference(customer_orders)
        return never_visited

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
