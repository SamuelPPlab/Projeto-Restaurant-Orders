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
        requested_set = set(list(requests))
        orders_set = set([row[1] for row in self.orders])
        return orders_set.difference(requested_set)

    def get_days_never_visited_per_costumer(self, costumer):
        days_set = set([row[2] for row in self.orders])
        requested_days_array = [
            row[2] for row in self.orders if row[0] == costumer
        ]
        requested_days_set = set(requested_days_array)
        return days_set.difference(requested_days_set)

    def get_busiest_day(self):
        days_dict = self.orders_by_day()
        return max(days_dict, key=days_dict.get)

    def get_least_busy_day(self):
        days_dict = self.orders_by_day()
        return min(days_dict, key=days_dict.get)

    def orders_by_user(self, costumer):
        food_counter = {}
        requested_food_array = [
            row[1] for row in self.orders if row[0] == costumer
        ]
        for requested_food in requested_food_array:
            if requested_food not in food_counter:
                food_counter[requested_food] = 1
            else:
                food_counter[requested_food] += 1

        return food_counter

    def orders_by_day(self):
        days_counter = {}
        for _, _, day in self.orders:
            if day not in days_counter:
                days_counter[day] = 1
            else:
                days_counter[day] += 1
        return days_counter
