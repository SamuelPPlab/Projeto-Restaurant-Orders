class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)


    def add_new_order(self, costumer, order, day):
        self.orders.append({'costumer': costumer, 'order': order, 'day': day})


    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_orders = {}

        for order in self.orders:
            if order['costumer'] == costumer:
                if order['order'] not in costumer_orders:
                    costumer_orders[order['order']] = 1
                else:
                    costumer_orders[order['order']] += 1
        
        # # source:
        # # https://stackoverflow.com/questions/42044090
        # # /return-the-maximum-value-from-a-dictionary/42044202
        max_value = max(costumer_orders.values())
        most_ordered_dish = [k for k, v in costumer_orders.items() if v == max_value]

        return most_ordered_dish[0]


    def get_never_ordered_per_costumer(self, costumer):
        all_orders = set()
        costumer_orders = set()

        never_ordered = set()

        for order in self.orders:
            if order['order'] not in all_orders:
                all_orders.add(order['order'])

            if order['costumer'] == costumer:
                if order['order'] not in costumer_orders:
                    costumer_orders.add(order['order'])

        for order in all_orders:
            if order not in costumer_orders:
                never_ordered.add(order)

        return never_ordered


    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        costumer_days = set()

        never_visited = set()

        for order in self.orders:
            if order['day'] not in all_days:
                all_days.add(order['day'])

            if order['costumer'] == costumer:
                if order['day'] not in costumer_days:
                    costumer_days.add(order['day'])

        for order in all_days:
            if order not in costumer_days:
                never_visited.add(order)

        return never_visited


    def get_busiest_day(self):
        days = {}

        for order in self.orders:
            if order['day'] not in days:
                days[order['day']] = 1
            else:
                days[order['day']] += 1
        
        max_value = max(days.values())
        busiest_day = [k for k, v in days.items() if v == max_value]

        return busiest_day[0]


    def get_least_busy_day(self):
        days = {}

        for order in self.orders:
            if order['day'] not in days:
                days[order['day']] = 1
            else:
                days[order['day']] += 1
        
        min_value = min(days.values())
        busiest_day = [k for k, v in days.items() if v == min_value]

        return busiest_day[0]
