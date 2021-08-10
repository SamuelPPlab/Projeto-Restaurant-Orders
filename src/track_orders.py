from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []
        self._data_len = 0

    def __len__(self):
        return self._data_len

    def add_new_order(self, costumer, order, day):
        self.orders.append(
            {"costumer": costumer, "order": order, "weekday": day}
        )
        self._data_len += 1

    def get_most_ordered_dish_per_costumer(self, costumer):
        counter = {}
        for item in self.orders:
            if item["costumer"] == costumer:
                counter[item["order"]] = counter.get(item["order"], 0) + 1
        most_ordered = Counter(counter).most_common(1)
        return (most_ordered[0])[0]

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

    def get_dish_quantity_per_costumer(self, costumer, order):
        pass
