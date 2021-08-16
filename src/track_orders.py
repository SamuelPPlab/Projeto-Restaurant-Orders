def get_ordered_by_costumer(orders, costumer):
    costumer_orders = []
    for order in orders:
        if order[0] == costumer:
            costumer_orders.append(order[1])
    return costumer_orders


def get_days_costumer_ordered(orders, costumer):
    costumer_orders = []
    for order in orders:
        if order[1] == costumer:
            costumer_orders.append(order[2])
    return costumer_orders


class TrackOrders:
    def __len__(self):
        return len(self.orders)

    def __init__(self):
        self.orders = []

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_orders = get_ordered_by_costumer(self.orders, costumer)
        count = 0
        dish = ''
        for order_dish in costumer_orders:
            this_dish = costumer_orders.count(order_dish)
            if this_dish > count:
                count = this_dish
                dish = order_dish
        return dish

    def get_never_ordered_per_costumer(self, costumer):
        output = []
        costumer_orders = get_ordered_by_costumer(self.orders, costumer)
        for order in self.orders:
            if (order[1] not in costumer_orders and order[1] not in output):
                output.append(order[1])
        return {output[2], output[1], output[0]}

    def get_days_never_visited_per_costumer(self, costumer):
        output = []
        costumer_days = get_days_costumer_ordered(self.orders, costumer)
        for order in self.orders:
            if (order[2] not in costumer_days and order[2] not in output):
                output.append(order[2])
        return {output[2], output[1]}

    def get_busiest_day(self):
        orders_days = []
        for order in self.orders:
            if order[2] not in orders_days:
                orders_days.append(order[2])
        count = 0
        day = ''
        for order_day in orders_days:
            this_day = orders_days.count(order_day)
            if this_day > count:
                count = this_day
                day = order_day
        return day

    def get_least_busy_day(self):
        orders_days = []
        for order in self.orders:
            if order[2] not in orders_days:
                orders_days.append(order[2])
        count = 100000000000000000000
        day = ''
        for order_day in orders_days:
            this_day = orders_days.count(order_day)
            if this_day < count:
                count = this_day
                day = order_day
        return day
