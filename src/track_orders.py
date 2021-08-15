class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, customer):
        most_asked_by_client = {}
        favorite_dish = ""
        times_asked = 0
        for (name, food, _) in self.orders:
            if name == customer:
                if food in most_asked_by_client:
                    most_asked_by_client[food] += 1
                else:
                    most_asked_by_client[food] = 1
                if most_asked_by_client[food] > times_asked:
                    favorite_dish = food
                    times_asked = most_asked_by_client[food]
        return favorite_dish

    def get_never_ordered_per_costumer(self, customer):
        dishes_asked_by_client = set()
        dishes = set()
        for (name, food, _) in self.orders:
            dishes.add(food)
            if name == customer:
                dishes_asked_by_client.add(food)
        return dishes.difference(dishes_asked_by_client)

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
