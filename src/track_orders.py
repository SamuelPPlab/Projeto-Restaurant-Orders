from collections import Counter


class TrackOrders:
    def __init__(self):
        self.get_orders = list()

    def __len__(self):
        return len(self.get_orders)

    def add_new_order(self, costumer, order, day):
        return self.get_orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_orders = list()
        for rows in self.get_orders:
            if (rows[0] == costumer):
                costumer_orders.append(rows[1])
        contador = Counter(costumer_orders)
        mais_pedido = contador.most_common(1)[0][0]
        return mais_pedido

    def get_never_ordered_per_costumer(self, costumer):
        costumer_orders = set()
        for rows in self.get_orders:
            if (rows[0] == costumer):
                costumer_orders.add(rows[1])
        all_foods = {"coxinha", "pizza", "hamburguer", "misto-quente"}
        return all_foods - costumer_orders

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_orders = set()
        for rows in self.get_orders:
            if (rows[0] == costumer):
                costumer_orders.add(rows[2])
        all_days = {"terça-feira", "segunda-feira", "sabado"}
        return all_days - costumer_orders

    def get_busiest_day(self):
        days = list()
        for rows in self.get_orders:
            days.append(rows[2])
        contador = Counter(days)
        mais_pedido = contador.most_common(1)[0][0]
        return mais_pedido

    def get_least_busy_day(self):
        days = list()
        repetition = list()
        for rows in self.get_orders:
            days.append(rows[2])
        contador = Counter(days)
        mais_pedido = contador.items()
        for index in mais_pedido:
            repetition.append(index[0])
        less_busy_day = repetition[len(repetition) - 1]
        return less_busy_day
