from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = {}

    def get_menu(self):
        menu = set()
        for value in self.orders.values():
            for food in value["foods"].keys():
                menu.add(food)
        return menu

    def get_days_open(self):
        days_open = set()
        for value in self.orders.values():
            for day in value["days"].keys():
                days_open.add(day)
        return days_open

    def print(self):
        for key, value in self.orders.items():
            print((f"{key}: {value}\n"))

    def __len__(self):
        return sum(sum(v["foods"].values()) for n, v in self.orders.items())

    def add_new_order(self, costumer, order, day):
        if costumer not in self.orders:
            self.orders[costumer] = {
                "days": {},
                "foods": {},
            }
        if day in self.orders[costumer]["days"]:
            self.orders[costumer]["days"][day] += 1
        else:
            self.orders[costumer]["days"].update({day: 1})

        if order in self.orders[costumer]["foods"]:
            self.orders[costumer]["foods"][order] += 1
        else:
            self.orders[costumer]["foods"].update({order: 1})

    def get_dish_quantity_per_costumer(self, costumer, order):
        return self.orders[costumer]["foods"][order]

    def get_most_ordered_dish_per_costumer(self, costumer):
        foods = self.orders[costumer]["foods"]
        return max(foods, key=foods.get)

    def get_never_ordered_per_costumer(self, costumer):
        menu = self.get_menu()
        return menu.difference(self.orders[costumer]["foods"].keys())

    def get_days_never_visited_per_costumer(self, costumer):
        days_open = self.get_days_open()
        return days_open.difference(self.orders[costumer]["days"].keys())

    def quantity_days_open_per_day(self):
        return sum(
            (Counter(costumer["days"]) for costumer in self.orders.values()),
            Counter(),  # initialize an empty Counter as initial value of sum
        )

    def get_busiest_day(self):
        days_open_per_day = self.quantity_days_open_per_day()
        return max(days_open_per_day, key=days_open_per_day.get)

    def get_least_busy_day(self):
        days_open_per_day = self.quantity_days_open_per_day()
        return min(days_open_per_day, key=days_open_per_day.get)
