class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        requests = self.orders_by_user(costumer)
        return max(requests, key=requests.get)

    def get_never_ordered_per_costumer(self, costumer):
        requests = self.orders_by_user(costumer)
        requested = set(list(requests))
        orders = set([row[1] for row in self.orders])
        return orders.difference(requested)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set([row[2] for row in self.orders])
        requested = [row[2] for row in self.orders if row[0] == costumer]
        requested_days = set(requested)
        return days.difference(requested_days)

    def get_busiest_day(self):
        day = self.orders_by_day()
        return max(day, key=day.get)

    def get_least_busy_day(self):
        days = self.orders_by_day()
        return min(days, key=days.get)

    def orders_by_user(self, costumer):
        foods = {}
        requestedFood = [row[1] for row in self.orders if row[0] == costumer]
        for food in requestedFood:
            if food not in foods:
                foods[food] = 1
            else:
                foods[food] += 1
        return foods

    def orders_by_day(self):
        days = {}
        for _, _, day in self.orders:
            if day not in days:
                days[day] = 1
            else:
                days[day] += 1
        return days
