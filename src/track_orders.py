class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def get_orders_by_customer(self, customer):
        return [
            order["order"] for order in self.orders
            if order["name"] == customer
        ]

    def add_new_order(self, costumer, order, day):
        self.orders.append({"name": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        result = self.get_orders_by_customer(costumer)
        return max(set(result), key=result.count)

    def get_never_ordered_per_costumer(self, costumer):
        result = set(self.get_orders_by_customer(costumer))
        return {order["order"] for order in self.orders}.difference(result)

    def get_days_never_visited_per_costumer(self, costumer):
        result = [
            order["day"] for order in self.orders if order["name"] == costumer
        ]
        return {order["day"] for order in self.orders}.difference(result)

    def get_busiest_day(self):
        days = dict()
        for order in self.orders:
            if order["day"] not in days:
                days[order["day"]] = 1
            else:
                days[order["day"]] += 1

        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = dict()
        for order in self.orders:
            if order["day"] not in days:
                days[order["day"]] = 1
            else:
                days[order["day"]] += 1

        return min(days, key=days.get)
