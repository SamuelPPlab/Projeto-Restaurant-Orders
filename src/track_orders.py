from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders_list = []

    def __len__(self):
        return len(self.orders_list)

    def add_new_order(self, costumer, order, day):
        self.orders_list.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders_by_user = [
            order[1] for order in self.orders_list if order[0] == costumer]
        return Counter(orders_by_user).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        orders = set([order[1] for order in self.orders_list])
        costumer_orders = set([
            order[1] for order in self.orders_list if order[0] == costumer])
        return orders.difference(costumer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        all_day = set([order[2] for order in self.orders_list])
        visited_days_by_user = set([
            order[2] for order in self.orders_list if order[0] == costumer])
        return all_day.difference(visited_days_by_user)

    def get_busiest_day(self):
        all_days = [order[2] for order in self.orders_list]
        most_commom_day = Counter(all_days).most_common(1)[0][0]
        return most_commom_day

    def get_least_busy_day(self):
        all_days = [order[2] for order in self.orders_list]
        least_common_day = Counter(all_days).most_common()[-1][0]
        return least_common_day
