from collections import Counter


class TrackOrders:
    def list_by_costumer(list_clients, costumer):
        list_costumer = []
        for item in list_clients:
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
        list_costumer = TrackOrders.list_by_costumer(self.order_list, costumer)
        return Counter(list_costumer).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = []
        for item in self.order_list:
            all_orders.append(item[1])
        list_costumer = TrackOrders.list_by_costumer(self.order_list, costumer)

        return all_orders.difference(list_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
