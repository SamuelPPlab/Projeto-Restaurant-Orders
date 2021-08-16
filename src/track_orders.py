from collections import Counter


class TrackOrders:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, costumer, order, day):
        return self.data.append({"name": costumer, "meal": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = []
        for order in self.data:
            if order["name"] == costumer:
                orders.append(order["meal"])
        return Counter(orders).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        customers_meals = set()
        all_meals = set()
        for order in self.data:
            all_meals.add(order["meal"])
            if(order["name"] == costumer):
                customers_meals.add(order["meal"])
        return all_meals.difference(customers_meals)

    def get_days_never_visited_per_costumer(self, costumer):
        customer_days = set()
        days = set()
        for order in self.data:
            days.add(order["day"])
            if order["name"] == costumer:
                customer_days.add(order["day"])
        return days.difference(customer_days)

    def get_days(self):
        return Counter(order['day'] for order in self.data)

    def get_busiest_day(self):
        return self.get_days().most_common(1)[0][0]

    def get_least_busy_day(self):
        return self.get_days().most_common()[-1][0]
