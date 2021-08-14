import operator


class TrackOrders:
    def __init__(self):
        self.orders = list()
        self.customer_orders = dict()
        self.foods = set()
        self.weekdays = dict()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.foods.add(order)
        self.orders.append([costumer, order, day])

        if costumer not in self.customer_orders:
            self.customer_orders[costumer] = {
                "foods": {order: 1}, "weekdays": {day: 1}}

        if day not in self.weekdays:
            self.weekdays[day] = 1
        else:
            self.weekdays[day] += 1

        if day not in self.customer_orders[costumer]["weekdays"]:
            self.customer_orders[costumer]["weekdays"][day] = 1
        else:
            self.customer_orders[costumer]["weekdays"][day] += 1

        if order not in self.customer_orders[costumer]["foods"]:
            self.customer_orders[costumer]["foods"][order] = 1
        else:
            self.customer_orders[costumer]["foods"][order] += 1

    def get_most_ordered_dish_per_costumer(self, costumer):
        return max(self.customer_orders[costumer]["foods"].items(),
                   key=operator.itemgetter(1))[0]

    def get_order_frequency_per_costumer(self, costumer, order):
        return self.customer_orders[costumer]["foods"][order]

    def get_never_ordered_per_costumer(self, costumer):
        return self.foods - (self.customer_orders[costumer]["foods"]).keys()

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_weekdays = {*self.customer_orders[costumer]["weekdays"]}
        weekdays = {*self.weekdays}

        return weekdays - costumer_weekdays

    def get_busiest_day(self):
        return max(self.weekdays.items(), key=operator.itemgetter(1))[0]

    def get_least_busy_day(self):
        return min(self.weekdays.items(), key=operator.itemgetter(1))[0]
