from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = {}
        self.days = set()

    def __len__(self):
        return sum(
            [
                sum(list(costumer["dishes"].values()))
                for costumer in self.orders.values()
            ]
        )

    def add_new_order(self, costumer, order, day):
        if costumer in self.orders:
            if order in self.orders[costumer]["dishes"]:
                self.orders[costumer]["dishes"][order] += 1
            else:
                self.orders[costumer]["dishes"][order] = 1
            if day in self.orders[costumer]["days"]:
                self.orders[costumer]["days"][day] += 1
            else:
                self.orders[costumer]["days"][day] = 1
        else:
            self.orders[costumer] = {"dishes": {order: 1}, "days": {day: 1}}
        self.days.add(day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return max(
            self.orders[costumer]["dishes"],
            key=self.orders[costumer]["dishes"].get,
        )

    def get_days_never_visited_per_costumer(self, costumer):
        return self.days.difference(self.orders[costumer]["days"].keys())

    def frequency_day(self):
        test = sum(
            (Counter(costumer["days"]) for costumer in self.orders.values()),
            Counter(),
        )
        return test

    def get_busiest_day(self):
        result = sum(
            (Counter(costumer["days"]) for costumer in self.orders.values()),
            Counter(),
        )
        return max(result, key=result.get)

    def get_least_busy_day(self):
        result = sum(
            (Counter(costumer["days"]) for costumer in self.orders.values()),
            Counter(),
        )
        return min(result, key=result.get)

    def get_dish_quantity_per_costumer(self, costumer, dish):
        return (
            self.orders[costumer]["dishes"][dish]
            if dish in self.orders[costumer]["dishes"]
            else 0
        )
