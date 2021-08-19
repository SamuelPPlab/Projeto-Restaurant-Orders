class TrackOrders:
    def __init__(self):
        self.orders = {}
        self.foods = set()
        self.days = set()
        self.days_count = {}

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        if costumer not in self.orders:
            self.orders[costumer] = {
              "foods": {order: 1}, "days": {day: 1}}

        if order not in self.orders[costumer]["foods"]:
            self.orders[costumer]["foods"][order] = 1
        else:
            self.orders[costumer]["foods"][order] += 1

        if day not in self.orders[costumer]["days"]:
            self.orders[costumer]["days"][day] = 1
        else:
            self.orders[costumer]["days"][day] += 1

        if day not in self.days:
            self.days_count[day] = 1
        else:
            self.days_count[day] += 1

        self.foods.add(order)
        self.days.add(day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        for food in self.orders[costumer]["foods"]:
            if self.orders[costumer]["foods"][food] == max(
              self.orders[costumer]["foods"].values()):
                return food

    def get_never_ordered_per_costumer(self, costumer):
        return self.foods.difference(self.orders[costumer]["foods"].keys())

    def get_days_never_visited_per_costumer(self, costumer):
        return self.days.difference(self.orders[costumer]["days"].keys())

    def get_busiest_day(self):
        for day in self.days_count:
            if self.days_count[day] == max(
              self.days_count.values()):
                return day

    def get_least_busy_day(self):
        for day in self.days_count:
            if self.days_count[day] == min(
              self.days_count.values()):
                return day
