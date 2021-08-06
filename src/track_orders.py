import collections


class TrackOrders:
    def __init__(self):
        self.pedidos = []

    def __len__(self):
        return len(self.pedidos)

    def add_new_order(self, customer, order, day):
        return self.pedidos.append({
            "name": customer,
            "order": order,
            "day": day
            })

    def get_order_frequency_per_costumer(self, customer):
        pass

    def get_most_ordered_dish_per_costumer(self, customer):
        customer_list = []
        for row in self.pedidos:
            # print(row)
            if row['name'] == customer:
                customer_list.append(row['order'])
        return collections.Counter(customer_list).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, customer):
        pass

    def get_days_never_visited_per_costumer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass


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
# track_orders = TrackOrders()
# for name, food, day in csv_parsed:
#    track_orders.add_new_order(name, food, day)
# most_ordered = track_orders.get_most_ordered_dish_per_costumer("maria")
# print(most_ordered)
