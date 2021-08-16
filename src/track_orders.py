import collections


class TrackOrders:
    def __init__(self):
        self.all_orders = []

    def __len__(self):
        # pass
        return len(self.all_orders)

    def add_new_order(self, costumer, order, day):
        # pass
        self.all_orders.append({
            'k1_custumer': costumer,
            'k2_ordered_dish': order,
            'k3_week_day': day
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        # pass
        ordered_dishs = [
            order['k2_ordered_dish']
            for order in self.all_orders
            if order['k1_custumer'] == costumer
        ]
        mostorderdish = collections.Counter(ordered_dishs).most_common(1)[0][0]
        return mostorderdish

    def get_never_ordered_per_costumer(self, costumer):
        # pass
        dishs_types = {
            order['k2_ordered_dish']
            for order in self.all_orders
        }
        ordered_dish_customer = {
            order['k2_ordered_dish']
            for order in self.all_orders
            if order['k1_custumer'] == costumer
        }
        dish_never_ordered = dishs_types ^ ordered_dish_customer
        return dish_never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        # pass
        get_all_days = {
            week_day['k3_week_day']
            for week_day in self.all_orders
        }
        days_in = {
            week_day['k3_week_day']
            for week_day in self.all_orders
            if week_day['k1_custumer'] == costumer
        }
        days_out = get_all_days ^ days_in
        return days_out

    def get_busiest_day(self):
        # pass
        days_in = [
            week_day['k3_week_day']
            for week_day in self.all_orders
        ]
        count_li = collections.Counter(days_in)
        busiest_day = list(count_li.keys())[0]
        return busiest_day

    def get_least_busy_day(self):
        pass
        days_in = [
            week_day['k3_week_day']
            for week_day in self.all_orders
        ]
        count_li = collections.Counter(days_in)
        busiest_day = list(count_li.keys())[-1]
        return busiest_day

# python3 -m pytest tests/test_track_orders.py
# referencias
