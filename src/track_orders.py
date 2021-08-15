import collections

c = collections.Counter()

'''Colaboração do amigo Éric
PR: https://github.com/tryber/sd-07-restaurant-orders/blob/
03cb8223d08678679e8ba211f98e5d3013f61d8e/src/track_orders.py'''


class TrackOrders:
    def __len__(self):
        return len(self.orders)

    def __init__(self):
        self.orders = []

    def add_new_order(self, costumer, order, day):
        self.orders.append({"name": costumer, "order": order, "day": day})
        return self.orders

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_ordered = []
        for order in self.orders:
            if order["name"] == costumer:
                most_ordered.append(order["order"])
        return collections.Counter(most_ordered).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        food = set()
        food_ordered = set()
        for order in self.orders:
            if(order["name"] == costumer):
                food_ordered.add(order["order"])
            food.add(order["order"])
        never_ordered = food.difference(food_ordered)
        return never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        days_visited = set()
        for order in self.orders:
            if(order["name"] == costumer):
                days_visited.add(order["day"])
            days.add(order["day"])
        days_never_visited = days.difference(days_visited)
        return days_never_visited

    def get_busiest_day(self):
        all_days = []
        for order in self.orders:
            all_days.append(order["day"])
        return collections.Counter(all_days).most_common(1)[0][0]

    def get_least_busy_day(self):
        all_days = []
        for order in self.orders:
            all_days.append(order["day"])
        return collections.Counter(all_days).most_common()[-1][0]
