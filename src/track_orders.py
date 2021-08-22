from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = list()
        

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"name": costumer, "meal": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        customer_orders = list()
        for order in self.orders:
            if order["name"] == costumer:
                customer_orders.append(order["meal"])
        orders_counted = Counter(customer_orders)
        # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        most_ordered = max(orders_counted, key=orders_counted.get)
        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        costomer_orders = list()
        never_ordered_list = list()
        meal_options = ["coxinha", "hamburguer", "misto-quente", "pizza"]

        for order in self.orders:
            if order["name"] == costumer:
                costomer_orders.append(order["meal"])
        for meal_option in meal_options:
            if meal_option not in costomer_orders:
                never_ordered_list.append(meal_option)

        return set(never_ordered_list)

    def get_days_never_visited_per_costumer(self, costumer):
        days_orders = list()
        never_going_days_list = list()
        days_options = ["sabado", "segunda-feira", "terça-feira"]

        for order in self.orders:
            if order["name"] == costumer:
                days_orders.append(order["day"])
        for meal_option in days_options:
            if meal_option not in days_orders:
                never_going_days_list.append(meal_option)
        return set(never_going_days_list)

    def get_busiest_day(self):
        days_orders = list()
        for order in self.orders:
            days_orders.append(order["day"])
        days_relatory = Counter(days_orders)
        # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        busiest_day = max(days_relatory, key=days_relatory.get)
        return busiest_day


    def get_least_busy_day(self):
        days_orders = list()
        for order in self.orders:
            days_orders.append(order["day"])
        days_relatory = Counter(days_orders)
        # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        least_busy = min(days_relatory, key=days_relatory.get)
        return least_busy
