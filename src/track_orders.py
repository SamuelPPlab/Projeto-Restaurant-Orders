from typing import Counter


class TrackOrders:
    def __init__(self):
        self.orders = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.add((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = 0
        mock_order = {}
        for order in range(len(self.all_order)):
            if self.all_order[order]["costumer"] == costumer:
                mock_order[
                    self.all_order[order]["order"]
                ] = self.all_order.count(self.all_order[order])
        for num in mock_order:
            if mock_order[num] > count:
                count = mock_order[num]
                self.most_ordered = num
        return self.most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        all_dishes = set()
        dishes = set()
        for request in self.orders:
            all_dishes.add(request['order'])
            if request['costumer'] == costumer:
                dishes.add(request['order'])
        return all_dishes.difference(dishes)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        client_days = set()

        for day in self.orders:
            all_days.add(day[2])
        for client in self.orders:
            if client[0] == costumer:
                client_days.add(client[2])
        return all_days.difference(client_days)

    def get_busiest_day(self):
        self.get_frequency()
        values, keys = list(self.frequency.values()), list(
            self.frequency.keys()
        )
        max_value = max(values)
        busiest_day = keys[values.index(max_value)]
        return busiest_day

    def get_least_busy_day(self):
        working_days = []
        for day in self.orders:
            working_days.append(day[2])
        emptiest_day = Counter(working_days).most_common()[-1][0]
        return emptiest_day
