from src.analyze_log import open_file, consult_most_frequent_order_by_client
from src.analyze_log import never_order_by_client
from src.analyze_log import days_never_attended_by_client


class TrackOrders:
    path = 'data/orders_1.csv'

    def __init__(self) -> None:
        self.track_orders = []

    def __len__(self):
        return len(self.track_orders)

    def add_new_order(self, costumer, order, day):
        self.track_orders.append(list((costumer, order, day)))

    def get_most_ordered_dish_per_costumer(self, costumer):
        data = open_file(self.path)
        return consult_most_frequent_order_by_client(data, costumer)

    def get_dish_quantity_per_costumer(self, costumer, dish):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        return never_order_by_client(self.track_orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return days_never_attended_by_client(self.track_orders, costumer)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass


if __name__ == "__main__":
    client = TrackOrders()
    client.add_new_order('renato', 'pizza', 'segunda')
    print(len(client))
    client.get_most_ordered_dish_per_costumer('maria')
    client.get_never_ordered_per_costumer("joao")
