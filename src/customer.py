class Costumer:

    name = ""
    order = []
    day = []

    def __init__(self, name, order, day):
        self.name = name
        self.order = []
        self.day = []
        self.order.append(order)
        self.day.append(day)

    def most_ordered_dish(self):
        return max(set(self.order), key=self.order.count)

    def get_dish_quantity(self, order):
        return list(filter(lambda x: x == order), self.order)

    def add_new_order(self, order):
        self.order.append(order)

    def add_new_day(self, day):
        self.day.append(day)
