from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        foods_orders = []

        for order in self.orders:
            if order[0] == costumer:
                foods_orders.append(order[1])

        return Counter(foods_orders).most_common(1)[0][0]

    def all_dishes(dish_list):
        dishes = []

        for order in dish_list:
            if order[1] not in dishes:
                dishes.append(order[1])

        return dishes

    def get_never_ordered_per_costumer(self, costumer):
        dish_counter = {}
        all_dishes = TrackOrders.all_dishes(self.orders)

        for order in self.orders:
            if order[0] == costumer:
                if order[1] not in dish_counter:
                    dish_counter[order[1]] = 1
                else:
                    dish_counter[order[1]] += 1

        dish_counted = set(dish_counter)
        dishes_ordered = set(all_dishes)

        return dishes_ordered.difference(dish_counted)

    def week_days(dish_list):
        all_days = []

        for order in dish_list:
            if order[2] not in all_days:
                all_days.append(order[2])

        return all_days

    def get_days_never_visited_per_costumer(self, costumer):
        attended = []
        days_week = TrackOrders.week_days(self.orders)

        for order in self.orders:
            if order[0] == costumer:
                if order[2] not in attended:
                    attended.append(order[2])

        all_days = set(days_week)
        customer_attended = set(attended)

        return all_days.difference(customer_attended)

    def get_busiest_day(self):
        all_days = []

        for order in self.orders:
            all_days.append(order[2])

        return Counter(all_days).most_common(1)[0][0]

    def get_least_busy_day(self):
        all_days = []

        for order in self.orders:
            all_days.append(order[2])

        return Counter(all_days).most_common()[-1][0]
