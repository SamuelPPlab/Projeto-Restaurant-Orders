from src.functions.fun_analyze import most_frequent_item
from src.functions.fun_analyze import number_of_dishes_per_person
from src.functions.fun_analyze import dishes_never_ordered_per_person
from src.functions.fun_analyze import days_person_not_go_cafeteria
from src.functions.fun_analyze import day_that_most_appears
from src.functions.fun_analyze import day_that_appears_less


class TrackOrders:
    def __init__(self):
        self.orders = []
        self.client_dishes = dict()
        self.client_days = dict()
        self.menu = set()
        self.days_of_week = set()
        self.every_days = []

    def __len__(self):
        return len(self.orders)

    def feed_system(self):
        for order in self.orders:
            self.menu.add(order[1])
            self.days_of_week.add(order[2])
            self.every_days.append(order[2])
            self.client_dishes[order[0]] = self.client_dishes.get(
                order[0], []
            ) + [order[1]]
            self.client_days[order[0]] = self.client_days.get(order[0], []) + [
                order[2]
            ]

    def clear_system(self):
        self.client_days.clear()
        self.client_dishes.clear()
        self.menu.clear()
        self.days_of_week.clear()

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        self.clear_system()
        self.feed_system()

    def get_order_frequency_per_costumer(self, costumer, order):
        return number_of_dishes_per_person(self.client_dishes[costumer], order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return most_frequent_item(self.client_dishes[costumer])

    def get_never_ordered_per_costumer(self, costumer):
        return dishes_never_ordered_per_person(
            self.menu, self.client_dishes[costumer]
        )

    def get_days_never_visited_per_costumer(self, costumer):
        return days_person_not_go_cafeteria(
            self.days_of_week, self.client_days[costumer]
        )

    def get_busiest_day(self):
        return day_that_most_appears(self.every_days)

    def get_least_busy_day(self):
        return day_that_appears_less(self.every_days)
