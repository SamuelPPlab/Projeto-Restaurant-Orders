from typing import Counter


class TrackOrders:

    def __init__(self):
        self.track = {}
        self.days = {}
        self.orders = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.add((costumer, order, day))
    
    def search_qtd(self, list):
        count = 0
        order_more_requeted = ""
        for item, qtd in list.items():
            if qtd > count:
                count = qtd
                order_more_requeted = item
        return order_more_requeted

    def get_most_ordered_dish_per_costumer(self, costumer):
        order = {}

        def filter_customer(x):
            return costumer in x

        orders_costumer = list(filter(filter_customer, self.orders))
        for client, order_client, day in orders_costumer:
            if order_client not in order:
                order[order_client] = set()
                order[order_client] = 0

            order[order_client] += 1

        return self.search_qtd(order)

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
        return [
            day
            for day in self.days.keys()
            if self.days[day] == max(self.days.values())
        ][0]

    def get_least_busy_day(self):
        working_days = []
        for day in self.orders:
            working_days.append(day[2])
        emptiest_day = Counter(working_days).most_common()[-1][0]
        return emptiest_day
