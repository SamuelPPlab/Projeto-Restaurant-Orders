from collections import Counter


class TrackOrders:
    def __len__(self):
        return 0

    def add_new_order(self, costumer, order, day):
        current_order = [costumer, order, day]
        self.order_list.append(current_order)

    """
    referência: https://stackoverflow.com/questions/3594514/
    how-to-find-most-common-elements-of-a-list/44481414
    """
    def get_most_ordered_dish_per_costumer(self, costumer):
        list_by_costumer = []
        for item in self.order_list:
            if costumer in item:
                list_by_costumer.append(item)
        return Counter(list_by_costumer).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
