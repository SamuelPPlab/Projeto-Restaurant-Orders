from collections import Counter


class TrackOrders:
    def __init__(self):
        self.order_list = list()

    def list_by_costumer(self, costumer):
        list_costumer = []
        for item in self.order_list:
            if costumer in item:
                list_costumer.append(item)
        return list_costumer

    def __len__(self):
        return len(self.order_list)

    def add_new_order(self, costumer, order, day):
        current_order = [costumer, order, day]
        self.order_list.append(current_order)

    """
    referência: https://stackoverflow.com/questions/3594514/
    how-to-find-most-common-elements-of-a-list/44481414
    """

    def get_most_ordered_dish_per_costumer(self, costumer):
        list_costumer = self.list_by_costumer(costumer)
        list_order_costumer = []
        for item in list_costumer:
            list_order_costumer.append(item[1])

        return Counter(list_order_costumer).most_common(1)[0][0]

    def get_all_days(self):
        all_days = []
        for item in self.order_list:
            all_days.append(item[2])
        return set(all_days)

    def get_all_order(self):
        all_orders = []
        for item in self.order_list:
            all_orders.append(item[1])
        return set(all_orders)

    def get_days_by_customer(self, list_costumer):
        days_customer = []
        for item in list_costumer:
            days_customer.append(item[2])
        return days_customer

    def get_order_by_customer(self, list_costumer):
        orders_customer = []
        for item in list_costumer:
            orders_customer.append(item[1])
        return orders_customer

    def get_never_ordered_per_costumer(self, costumer):
        list_costumer = self.list_by_costumer(costumer)
        orders_customer = self.get_order_by_customer(list_costumer)
        return self.get_all_order().difference(orders_customer)

    def get_days_never_visited_per_costumer(self, costumer):
        list_costumer = self.list_by_costumer(costumer)
        days_customer = self.get_days_by_customer(list_costumer)
        return self.get_all_days().difference(days_customer)

    def get_busiest_day(self):
        return Counter(self.order_list).most_common()[0][0]

    def get_least_busy_day(self):
        return Counter(self.get_all_days()).most_common()[-1][0]

    def get_dish_quantity_per_costumer(self, costumer, order):
        list_costumer = self.list_by_costumer(costumer)
        list_order_costumer = []
        for item in list_costumer:
            list_order_costumer.append(item[1])
        return len(list_order_costumer)
