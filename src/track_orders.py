class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        food_requested = self.food_requested(costumer)
        return max(food_requested, key=food_requested.get)

    def get_dish_quantity_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        food = self.food_requested(costumer)
        menu = self.get_menu()
        food_never_requested = set()
        for item in menu:
            if item not in food:
                food_never_requested.add(item)
        return food_never_requested

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

    def food_requested(self, costumer):
        food_requested = {}
        for row in self.orders:
            if row[0] == costumer:
                if row[1] in food_requested:
                    food_requested[row[1]] += 1
                else:
                    food_requested[row[1]] = 1
        return food_requested

    def get_menu(self):
        menu = set()
        for row in self.orders:
            if row[1] not in menu:
                menu.add(row[1])
        return menu
