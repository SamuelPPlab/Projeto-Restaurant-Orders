class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = {}
        most_frequent = 0
        food = ""
        for row in self.orders:
            if row[0] == costumer:
                if row[1] not in count:
                    count[row[1]] = 1
                else:
                    count[row[1]] += 1
                if count[row[1]] > most_frequent:
                    most_frequent = count[row[1]]
                    food = row[1]
        return food

    def get_never_ordered_per_costumer(self, costumer):
        foods = set()
        count_foods = set()
        for a, b, c in self.orders:
            if a == costumer:
                count_foods.add(b)
            foods.add(b)
        return foods.symmetric_difference(count_foods)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        count_days = set()
        for a, b, c in self.orders:
            if a == costumer:
                count_days.add(c)
            days.add(c)
        return days.symmetric_difference(count_days)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

    def get_dish_quantity_per_costumer(self, user, food):
        pass
