class TrackOrders:
    def __init__(self):
        self.orders_file = list()

    def __len__(self):
        return len(self.orders_file)

    def add_new_order(self, costumer, order, day):
        self.orders_file.append([costumer, order, day])

    def get_most_ordered_dish(self, costumer):
        highest_orders = ""
        orders = {}
        for name, order, day in self.orders_file:
            if name == costumer:
                if order not in orders:
                    orders[order] = 1
                else:
                    orders[order] += 1
                if (
                    highest_orders not in orders
                    or orders[highest_orders] < orders[order]
                ):
                    highest_orders = order
        return highest_orders

    def get_frequency_by_customer(self, costumer, order):
        count_order = 0
        for request in self.orders_file:
            if request[0] == costumer:
                if request[1] == order:
                    count_order += 1
        return count_order

    def do_not_have_order(self, client, dish):
        super_set = set()
        sub_set = set()
        for order in self.orders_file:
            super_set.add(order[dish])
            if order[0] == client:
                sub_set.add(order[dish])
        dont_have_order = super_set.difference(sub_set)
        return dont_have_order

    def never_oredered(self, costumer):
        never_ordered = self.do_not_have_order(costumer, 1)
        return never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        never_visited = self.do_not_have_order(costumer, 2)
        return never_visited

    def get_busiest_day(self):
        count_days = {}
        busiest_day = self.orders_file[0][2]
        for order in self.orders_file:
            if order[2] not in count_days:
                count_days[order[2]] = 1
            else:
                count_days[order[2]] += 1
            if count_days[order[2]] > count_days[busiest_day]:
                busiest_day = count_days[order[2]]
        return busiest_day

    def get_least_busy_day(self):
        count_days = {}
        least_busy_day = self.orders_file[0][2]
        for order in self.orders_file:
            if order[2] not in count_days:
                count_days[order[2]] = 1
            else:
                count_days[order[2]] += 1
            if count_days[order[2]] <= count_days[least_busy_day]:
                least_busy_day = order[2]
        return least_busy_day
