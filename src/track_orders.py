import collections


class TrackOrders:
    def __len__(self):
        return len(self.pedidos)

    def __init__(self):
        self.pedidos = []

    def add_new_order(self, costumer, order, day):
        return self.pedidos.append(
            {"name": costumer, "order": order, "day": day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        order_list = []
        for item in self.pedidos:
            if item["name"] == costumer:
                order_list.append(item.order)
        return collections.Counter(order_list).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        all_dishes = set()
        costumer_dishes = set()
        for pedido in self.pedidos:
            all_dishes.add(pedido["order"])
            if pedido["name"] == costumer:
                costumer_dishes.add(pedido["order"])
        return all_dishes.difference(costumer_dishes)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        costumer_day = set()
        for pedido in self.pedidos:
            all_days.add(pedido["day"])
            if pedido["name"] == costumer:
                costumer_day.add(pedido["day"])
            return all_days.difference(costumer_day)

    def get_busiest_day(self):
        all_days = []
        for pedido in self.pedidos:
            all_days.append(pedido["day"])
        return collections.Counter(all_days).most_common(1)[0][0]

    def get_least_busy_day(self):
        all_days = []
        for pedido in self.pedidos:
            all_days.append(pedido["day"])
        return collections.Counter(all_days).most_common()[-1][0]
