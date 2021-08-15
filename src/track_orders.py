from src.analyze_log import most_request_food


class TrackOrders:
    def __init__(self):
        self.data_list = []

    def __len__(self):
        return len(self.data_list)

    def add_new_order(self, costumer, order, day):
        return self.data_list.append(
            {"name": costumer, "order": order, "day": day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        client_orders = []
        for line in self.data_list:
            if line["name"] == costumer:
                client_orders.append(line["order"])
        return most_request_food(client_orders)

    def get_never_ordered_per_costumer(self, costumer):
        menu = set()
        client_orders = set()
        for item in self.data_list:
            menu.add(item["order"])

        for item in self.data_list:
            if item["name"] == costumer:
                client_orders.add(item["order"])

        return menu.difference(client_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        week_days = set()
        client_visit_days = set()
        for item in self.data_list:
            week_days.add(item["day"])

        for item in self.data_list:
            if item["name"] == costumer:
                client_visit_days.add(item["day"])

        return week_days.difference(client_visit_days)

    def get_busiest_day(self):
        clients_visits = dict()
        week_day = False
        for day in self.data_list:
            if day["day"] in clients_visits:
                clients_visits[day["day"]] += 1
            else:
                clients_visits[day["day"]] = 1
        if (
            not week_day
            or clients_visits[day["day"]] > clients_visits[week_day]
        ):
            week_day = day["day"]
        return week_day

    def get_least_busy_day(self):
        clients_visits = dict()
        week_day = False
        for day in self.data_list:
            if day["day"] in clients_visits:
                clients_visits[day["day"]] += 1
            else:
                clients_visits[day["day"]] = 1
        if (
            not week_day
            or clients_visits[day["day"]] < clients_visits[week_day]
        ):
            week_day = day["day"]
        return week_day
