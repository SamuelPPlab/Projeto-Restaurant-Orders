from collections import Counter


class TrackOrders:
    def __init__(self):
        self.order_list = []
        self.order_menu = set()
        self.order_days = set()
        self.to_counter_days = []

    def __len__(self):
        pass

    def add_new_order(self, costumer, order, day):
        self.order_list.append({
            "costumer": costumer,
            "order": order,
            "day": day
        })
        self.order_menu.add(order)
        self.order_days.add(day)
        self.to_counter_days.append(day)

    def order_by_client(self, client, list_dict):
        def filter_client(dict):
            if dict["costumer"] == client:
                return True
            return False
        return list(filter(filter_client, list_dict))

    def counter_food(sef, list_by_costumer):
        food_list = []
        for order in list_by_costumer:
            food_list.append(order['order'])
        return Counter(food_list).most_common()

    def get_most_ordered_dish_per_costumer(self, costumer):
        list_by_costumer = self.order_by_client(costumer, self.order_list)
        return self.counter_food(list_by_costumer)[0][0]

    def set_day_list(self, order_list):
        set_day = set()
        for order in order_list:
            set_day.add(order['day'])
        return set_day

    def get_never_ordered_per_costumer(self, costumer):
        food_set = set()
        list_by_costumer = self.order_by_client(costumer, self.order_list)
        food_by_client = self.counter_food(list_by_costumer)
        for food in food_by_client:
            food_set.add(food[0])
        return self.order_menu.difference(food_set)

    def get_days_never_visited_per_costumer(self, costumer):
        list_by_costumer = self.order_by_client(costumer, self.order_list)
        set_days_food = self.set_day_list(list_by_costumer)
        return self.order_days.difference(set_days_food)

    def get_busiest_day(self):
        return Counter(self.to_counter_days).most_common()[0][0]

    def get_least_busy_day(self):
        counter_days = Counter(self.to_counter_days).most_common()
        return counter_days[len(counter_days) - 1][0]
