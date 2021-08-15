from src.analyze_log import (
    client_didnt_show_up,
    client_never_ordered,
    most_common_order_by_client,
    busiest_day,
    least_busy_day,
)


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append(
            {"name": costumer, "order": order, "day_in_week": day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        return most_common_order_by_client(self.orders, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return client_never_ordered(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return client_didnt_show_up(self.orders, costumer)

    def get_busiest_day(self):
        return busiest_day(self.orders)

    def get_least_busy_day(self):
        return least_busy_day(self.orders)
