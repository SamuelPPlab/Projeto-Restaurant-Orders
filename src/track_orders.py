from collections import Counter


class TrackOrders:
    def __init__(self):
        self.list_orders = list()

    def __len__(self):
        return len(self.list_orders)

    def add_new_order(self, costumer, order, day):
        new_order = [costumer, order, day]
        self.list_orders.append(new_order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        list_order_client = [
            order[1] for order in self.list_orders if order[0] == costumer
        ]
        most_ordered_dish = Counter(list_order_client).most_common(1)[0][0]
        return most_ordered_dish

    def get_never_ordered_per_costumer(self, costumer):
        list_all_orders = set([order[1] for order in self.list_orders])

        list_order_client = set(
            [order[1] for order in self.list_orders if order[0] == costumer]
        )

        return list_all_orders.difference(list_order_client)

    def get_dish_quantity_per_costumer(self, costumer, order):
        list_order_client = [
            dish[1]
            for dish in self.list_orders
            if dish[0] == costumer and dish[1] == order
        ]

        return len(list_order_client) if list_order_client else 0

    def get_days_never_visited_per_costumer(self, costumer):
        list_all_days = set([order[2] for order in self.list_orders])

        list_days_client = set(
            [order[2] for order in self.list_orders if order[0] == costumer]
        )

        return list_all_days.difference(list_days_client)

    def get_busiest_day(self):
        list_all_days = [order[2] for order in self.list_orders]
        most_repeated_day = Counter(list_all_days).most_common(1)[0][0]
        return most_repeated_day

    def get_least_busy_day(self):
        list_all_days = [order[2] for order in self.list_orders]
        less_repeated_day = Counter(list_all_days).most_common()[-1][0]
        return less_repeated_day


if __name__ == "__main__":
    csv_parsed = [
        ["maria", "pizza", "terça-feira"],
        ["maria", "hamburguer", "terça-feira"],
        ["joao", "hamburguer", "terça-feira"],
        ["maria", "coxinha", "segunda-feira"],
        ["arnaldo", "misto-quente", "terça-feira"],
        ["jose", "hamburguer", "sabado"],
        ["maria", "hamburguer", "terça-feira"],
        ["maria", "hamburguer", "terça-feira"],
        ["joao", "hamburguer", "terça-feira"],
    ]

    track_orders = TrackOrders()
    for name, food, day in csv_parsed:
        track_orders.add_new_order(name, food, day)

    print(track_orders.get_most_ordered_dish_per_costumer("maria"))
    print(track_orders.get_never_ordered_per_costumer("joao"))
    print(track_orders.get_days_never_visited_per_costumer("joao"))
    print(track_orders.get_busiest_day())
    print(track_orders.get_least_busy_day())
    print(
        track_orders.get_dish_quantity_per_costumer("arnald", "misto-quente")
    )
