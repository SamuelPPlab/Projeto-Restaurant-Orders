import csv


class TrackOrders:
    def __init__(self) -> None:
        self.track_orders = []

    def __len__(self):
        return len(self.track_orders)

    def add_new_order(self, costumer, order, day):
        with open('data/orders_1.csv', "a") as file:
            writer = csv.writer(file)
            row = list((costumer, order, day))
            writer.writerow(row)
            self.track_orders.append(row)

    def get_most_ordered_dish_per_costumer(self, costumer):
        pass

    def get_dish_quantity_per_costumer(self, costumer, dish):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass


if __name__ == "__main__":
    client = TrackOrders()
    client.add_new_order('renato', 'pizza', 'segunda')
    print(len(client))
