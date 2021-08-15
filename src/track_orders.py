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

    def filter_days_of_the_week_not_repeated_in_list(array):
        new_list = []
        for item in array:
            if item[2] not in new_list:
                new_list.append(item[2])
        return new_list

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

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = []
        for item in self.order_list:
            all_orders.append(item[1])
        list_costumer = self.list_by_costumer(costumer)

        return all_orders.difference(list_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        list_costumer = self.list_by_costumer(costumer)
        days = self.filter_days_of_the_week_not_repeated_in_list(list_costumer)
        return list_costumer.difference(days)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
