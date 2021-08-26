class TrackOrders:
    def __len__(self):
        return len(self.orders)

    def __init__(self):
        self.orders = {}
        self.meals = list()
        self.open_days = list()

    def handle_existing_client(self, costumer, order, day):
        if order not in self.orders[costumer]['meals']:
            self.orders[costumer]['meals'].update({
                order: 1,
            })
        else:
            self.orders[costumer]['meals'][order] += 1

        if day not in self.orders[costumer]['days']:
            self.orders[costumer]['days'].update({
                day: 1
            })
        else:
            self.orders[costumer]['days'][day] += 1
        return self.orders[costumer]

    def add_new_order(self, costumer, order, day):
        if order not in self.meals:
            self.meals.append(order)
        if day not in self.open_days:
            self.open_days.append(day)
        # if costumer not in self.client_list:
        #     self.client_list.update(costumer)
        if costumer not in self.orders:
            return self.orders.update({costumer: {
                'meals': {order: 1},
                'days': {day: 1}
            }})
        return self.handle_existing_client(costumer, order, day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return max(
            self.orders[costumer]['meals'],
            key=self.orders[costumer]['meals'].get
        )

    def get_never_ordered_per_costumer(self, costumer):
        never_ordered = set()
        for m in self.meals:
            try:
                self.orders[costumer]['meals'][m]
            except(KeyError):
                never_ordered.add(m)
        return never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        never_visited = set()
        for d in self.open_days:
            try:
                self.orders[costumer]['days'][d]
            except(KeyError):
                never_visited.add(d)
        return never_visited

    def get_busiest_day(self):
        days_sum = {}
        for d in self.open_days:
            days_sum.update({d: 0})
        for c in self.orders.keys():
            for d in self.orders[c]['days']:
                days_sum[d] += self.orders[c]['days'][d]
        return max(days_sum, key=days_sum.get)

    def get_least_busy_day(self):
        days_sum = {}
        for d in self.open_days:
            days_sum.update({d: 0})
        for c in self.orders.keys():
            for d in self.orders[c]['days']:
                days_sum[d] += self.orders[c]['days'][d]
        return min(days_sum, key=days_sum.get)
