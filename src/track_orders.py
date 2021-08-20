from collections import Counter


class TrackOrders:
    def __init__(self):
        self.__orders = []

    def __len__(self):
        return len(self.__orders)

    def add_new_order(self, costumer, order, day):
        self.__orders.append(
            {"costumer": costumer, "product": order, "weekday": day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        customer_orders = [
            order["product"]
            for order in self.__orders
            if order["costumer"] == costumer
        ]
        count_orders = Counter(customer_orders)
        most_frequent = count_orders.most_common(1)[0][0]
        return most_frequent

    def get_order_frequency_per_costumer(self, costumer, order):
        customer_orders = [
            order["product"]
            for order in self.__orders
            if order["costumer"] == costumer
        ]
        count_orders = Counter(customer_orders)
        return count_orders[order]

    def get_never_ordered_per_costumer(self, costumer):
        menu_from_orders = {order["product"] for order in self.__orders}
        costumer_products_ordered = {
            order["product"]
            for order in self.__orders
            if order["costumer"] == costumer
        }
        return menu_from_orders.difference(costumer_products_ordered)

    def get_days_never_visited_per_costumer(self, costumer):
        weekdays_from_orders = {order["weekday"] for order in self.__orders}
        client_weekdays_ordered = {
            order["weekday"]
            for order in self.__orders
            if order["costumer"] == costumer
        }
        return weekdays_from_orders.difference(client_weekdays_ordered)

    def get_busiest_day(self):
        weekdays_orders = {}
        for order in self.__orders:
            weekdays_orders[order["weekday"]] = (
                weekdays_orders.get(order["weekday"], 0) + 1
            )
        return max(weekdays_orders, key=lambda key: weekdays_orders[key])

    def get_least_busy_day(self):
        weekdays_orders = {}
        for order in self.__orders:
            weekdays_orders[order["weekday"]] = (
                weekdays_orders.get(order["weekday"], 0) + 1
            )
        return min(weekdays_orders, key=lambda key: weekdays_orders[key])
