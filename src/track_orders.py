class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        asked_by_client = {}
        favorite_food = ""
        times_asked = 0
        for (name, food, _) in self.orders:
            if name == costumer:
                if food in asked_by_client:
                    asked_by_client[food] += 1
                else:
                    asked_by_client[food] = 1

                if asked_by_client[food] > times_asked:
                    favorite_food = food
                    times_asked = asked_by_client[food]
        return favorite_food

    def get_never_ordered_per_costumer(self, costumer):
        asked_by_client = set()
        all_foods = set()
        for (name, food, _) in self.orders:
            all_foods.add(food)
            if name == costumer:
                asked_by_client.add(food)
        return all_foods.difference(asked_by_client)

    def get_days_never_visited_per_costumer(self, costumer):
        days_client_go = set()
        all_days = set()
        for (name, _, day) in self.orders:
            all_days.add(day)
            if name == costumer:
                days_client_go.add(day)
        return all_days.difference(days_client_go)

    def get_busiest_day(self):
        clients_by_day = {}
        busiest_day = ""
        costumers_at_busiest_day = 0
        for (_, _, day) in self.orders:
            if day in clients_by_day:
                clients_by_day[day] += 1
            else:
                clients_by_day[day] = 1
            if clients_by_day[day] > costumers_at_busiest_day:
                busiest_day = day
                costumers_at_busiest_day = clients_by_day[day]
        return busiest_day

    def get_least_busy_day(self):
        clients_by_day = {}
        for (_, _, day) in self.orders:
            if day in clients_by_day:
                clients_by_day[day] += 1
            else:
                clients_by_day[day] = 1
        return min(clients_by_day, key=clients_by_day.get)
