class TrackOrders:
    def __len__(self):
        return self.pedidos

    def __init__(self):
        self.constumers = {}
        self.menu = set()
        self.days = set()
        self.all_days = []
        self.pedidos = 0

    def add_new_order(self, costumer, order, day):
        self.pedidos += 1
        self.all_days.append(day)
        self.menu.add(order)
        self.days.add(day)
        if costumer in self.constumers:
            self.constumers[costumer].append([order, day])
        else:
            self.constumers[costumer] = [[order, day]]

    def get_most_ordered_dish_per_costumer(self, costumer):
        array = []
        for i in self.constumers[costumer]:
            array.append(i[0])
        # magia \/
        return max(array, key=array.count)

    def get_never_ordered_per_costumer(self, costumer):
        menucopia = self.menu.copy()
        for order in self.constumers[costumer]:
            menucopia.discard(order[0])
        return menucopia

    def get_days_never_visited_per_costumer(self, costumer):
        dayscopia = self.days.copy()
        for order in self.constumers[costumer]:
            dayscopia.discard(order[1])
        return dayscopia

    def get_busiest_day(self):
        return max(self.all_days, key=self.all_days.count)

    def get_least_busy_day(self):
        return min(self.all_days, key=self.all_days.count)
