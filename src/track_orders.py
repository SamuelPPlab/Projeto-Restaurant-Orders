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
        result = []
        for i in self.pedidos:
            if i["name"] == costumer:
                result.append(i["order"])
        return collections.Counter(result).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        all_dish = set()
        costumer_dish = set()
        for pedido in self.pedidos:
            all_dish.add(pedido["order"])
            if pedido["name"] == costumer:
                costumer_dish.add(pedido["order"])
        return all_dish.difference(costumer_dish)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        costumer_day = set()
        for pedido in self.pedidos:
            all_days.add(pedido["day"])
            if pedido["name"] == costumer:
                costumer_day.add(pedido["day"])
        return all_days.difference(costumer_day)

    def get_busiest_day(self):
        days = []
        for pedido in self.pedidos:
            days.append(pedido["day"])
        return collections.Counter(days).most_common(1)[0][0]

    def get_least_busy_day(self):
        days = []
        for pedido in self.pedidos:
            days.append(pedido["day"])
        return collections.Counter(days).most_common()[-1][0]
