# import collections


import collections


class TrackOrders:
    def __len__(self):
        return len(self.demand)

    def __init__(self):
        self.demand = []

    def add_new_order(self, costumer, order, day):
        return self.demand.append(
            {"name": costumer, "dish": order, "week_day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        requests = []
        for item in self.demand:
            if item["name"] == costumer:
                requests.append(item["dish"])
        return collections.Counter(requests).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        list_dish = set()
        costumer_list_dish = set()
        for item in self.demand:
            list_dish.add(item["dish"])
            if item["name"] == costumer:
                costumer_list_dish.add(item["dish"])
        return list_dish.difference(costumer_list_dish)

    def get_days_never_visited_per_costumer(self, costumer):
        week = set()
        costumer_week_day = set()
        for item in self.demand:
            week.add(item["week_day"])
            if item["name"] == costumer:
                costumer_week_day.add(item["week_day"])
        return week.difference(costumer_week_day)

    def get_busiest_day(self):
        requests = []
        for item in self.demand:
            requests.append(item["week_day"])
        return collections.Counter(requests).most_common(1)[0][0]

    def get_least_busy_day(self):
        requests = []
        for item in self.demand:
            requests.append(item["week_day"])
        return collections.Counter(requests).most_common()[-1][0]


csv_parsed = [
    ["maria", "pizza", "terça-feira"],
    ["maria", "hamburguer", "terça-feira"],
    ["joao", "hamburguer", "terça-feira"],
    ["maria", "coxinha", "segunda-feira"],
    ["arnaldo", "misto-quente", "terça-feira"],
    ["jose", "hamburguer", "sabado"],
    ["maria", "hamburguer", "terça-feira"],
    ["maria", "hamburguer", "terça-feira"],
    ["joao", "hamburguer", "terça-feira"],
]
track_orders = TrackOrders()
for name, food, day in csv_parsed:
    track_orders.add_new_order(name, food, day)
less_busy = track_orders.get_most_ordered_dish_per_costumer("maria")
print(less_busy)
