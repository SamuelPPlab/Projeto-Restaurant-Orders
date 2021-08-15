import operator


class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append({
            "name": costumer,
            "order": order,
            "day": day,
            })

    def get_most_ordered_dish_per_costumer(self, costumer):
        freq_order = {}
        for name in self.orders:
            if(name["name"] == costumer):
                if (name["order"] in freq_order):
                    freq_order[name["order"]] += 1
                else:
                    freq_order[name["order"]] = 1
        return max(freq_order.items(), key=operator.itemgetter(1))[0]

    def get_never_ordered_per_costumer(self, costumer):
        history_client = set()
        items_menu = set()

        for order in self.orders:
            items_menu.add(order['order'])

        for order in self.orders:
            if order["name"] == costumer:
                history_client.add(order["order"])
        return set(items_menu) - set(history_client)

    def get_days_never_visited_per_costumer(self, costumer):
        days_week = set()
        days_in_snack_bar = set()
        for days in self.orders:
            days_week.add(days['day'])
        for days in self.orders:
            if days["name"] == costumer:
                days_in_snack_bar.add(days["day"])
        return set(days_week) - set(days_in_snack_bar)

    def get_busiest_day(self):
        freq_day = {}
        for day in self.orders:
            if (day["day"] in freq_day):
                freq_day[day["day"]] += 1
            else:
                freq_day[day["day"]] = 1
        return max(freq_day.items(), key=operator.itemgetter(1))[0]

    def get_least_busy_day(self):
        freq_day = {}
        for day in self.orders:
            if (day["day"] in freq_day):
                freq_day[day["day"]] += 1
            else:
                freq_day[day["day"]] = 1
        return min(freq_day.items(), key=operator.itemgetter(1))[0]
