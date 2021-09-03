import collections


class TrackOrders:
    def __len__(self):
        return len(self.orders)

    def __init__(self):
        self.orders = []

    def add_new_order(self, costumer, order, day):
        return self.orders.append(
            {"name": costumer, "order": order, "day": day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        list = []

        for row in self.orders:
            if row["name"] == costumer:
                list.append(row["order"])
        return collections.Counter(list).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        list_dishes = set()
        costumer_dishes = set()

        for row in self.orders:
            if row["name"] == costumer:
                costumer_dishes.add(row["order"])
            list_dishes.add(row["order"])
        return list_dishes.difference(costumer_dishes)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        frequency = set()

        for row in self.orders:
            if row["name"] == costumer:
                frequency.add(row["day"])
            days.add(row["day"])
        return days.difference(frequency)

    def get_busiest_day(self):
        days = []

        for row in self.orders:
            days.append(row["day"])

        return collections.Counter(days).most_common(1)[0][0]

    def get_least_busy_day(self):
        days = []

        for row in self.orders:
            days.append(row["day"])

        return collections.Counter(days).most_common()[-1][0]
