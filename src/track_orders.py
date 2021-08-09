# from analyze_log import AnalyzeDataByPerson


class TrackOrders:
    def __init__(self):
        self.stats = {}
        self.days = {}
        self.orders = set()

    def __len__(self):
        return len(self.stats)

    def add_new_order(self, costumer, order, day):
        if costumer not in self.stats:
            self.stats[costumer] = {"orders": {order: 1}, "days": set()}
        if order not in self.stats[costumer]["orders"].keys():
            self.stats[costumer]["orders"][order] = 1
        else:
            self.stats[costumer]["orders"][order] += 1
        if day not in self.days:
            self.days[day] = 1
        else:
            self.days[day] += 1
        self.orders.add(order)
        self.stats[costumer]["days"].add(day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        for order in self.stats[costumer]["orders"].keys():
            if self.stats[costumer]["orders"][order] == max(
                self.stats[costumer]["orders"].values()
            ):
                return order

    def get_never_ordered_per_costumer(self, costumer):
        return self.orders.difference(self.stats[costumer]["orders"].keys())

    def get_days_never_visited_per_costumer(self, costumer):
        return set(self.days.keys()).difference(self.stats[costumer]["days"])

    def get_busiest_day(self):
        for day in self.days.keys():
            if self.days[day] == max(self.days.values()):
                return day

    def get_least_busy_day(self):
        for day in self.days.keys():
            if self.days[day] == min(self.days.values()):
                return day
