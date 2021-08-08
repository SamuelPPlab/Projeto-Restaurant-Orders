import csv


class TrackOrders:
    def __init__(self):
        self.orders = []

    def get_orders(self):
        with open('data/orders_1.csv', 'r') as logs:
            reader = csv.reader(logs, delimiter=',')
            orders = [item for item in reader]

        return orders

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = self.orders
        count = {}
        costumer_orders = [item[1] for item in orders if item[0] == costumer]
        most_frequent = costumer_orders[0]

        for order in costumer_orders:
            if order not in count:
                count[order] = costumer_orders.count(order)
            if count[order] > count[most_frequent]:
                most_frequent = order

        return most_frequent

    def get_order_frequency_per_costumer(self, costomer, order):
        pass

    def get_never_ordered_per_costumer(self, custumer):
        orders = self.orders
        customer_plates = [item[1] for item in orders if item[0] == custumer]
        never_ordered = [
            item[1]
            for item in orders if customer_plates.count(item[1]) == 0
        ]

        return set(never_ordered)

    def get_days_never_visited_per_costumer(self, costumer):
        orders = self.orders
        days_visited = [item[2] for item in orders if item[0] == costumer]
        days = [item[2] for item in orders]
        never_visited = [
            day
            for day in days if days_visited.count(day) == 0
        ]

        return set(never_visited)

    def get_busiest_day(self):
        orders = self.orders
        count = {}
        orders_by_day = [item[2] for item in orders]
        most_frequent = orders_by_day[0]
        for order in orders_by_day:
            if order not in count:
                count[order] = orders_by_day.count(order)
            if count[order] > count[most_frequent]:
                most_frequent = order

        return most_frequent

    def get_least_busy_day(self):
        orders = self.orders
        count = {}
        orders_by_day = [item[2] for item in orders]

        less_frequent = orders_by_day[0]

        for order in orders_by_day:
            if order not in count:
                count[order] = orders_by_day.count(order)
            if count[order] < count[less_frequent]:
                less_frequent = order

        return less_frequent
