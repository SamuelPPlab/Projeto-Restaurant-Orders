class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        dish_per_costumer = dict()
        for item in self.orders:
            if costumer in item["costumer"]:
                dish_per_costumer[item["order"]] = 1
            else:
                dish_per_costumer[item["order"]] += 1
                return max(dish_per_costumer, key=dish_per_costumer.get)

    def get_never_ordered_per_costumer(self, costumer):
        meals = set()
        order = set()
        for item in self.orders:
            meals.add(item["order"])
            if item["costumer"] == costumer:
                order.add(item["order"])
        return meals.difference(order)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        client_ordered_days = set()
        for item in self.orders:
            days.add(item["day"])
            if costumer in item["costumer"]:
                client_ordered_days.add(item["day"])
        return days - client_ordered_days

    def get_busiest_day(self):
        days = dict()
        for item in self.orders:
            if item["day"] not in days:
                days[item["day"]] = 1
            else:
                days[item["day"]] += 1
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = dict()
        for item in self.orders:
            if item["day"] not in days:
                days[item["day"]] = 1
            else:
                days[item["day"]] += 1
        return min(days, key=days.get)
