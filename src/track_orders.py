class TrackOrders:
    def __init__(self):
        self.orders = []
    
    def __len__(self):
        return len(self.orders)
    
    def resume_orders_food_customer(self, customer):
        resume_orders_food = {}
        foods = [order[1] for order in self.orders if order[0] == customer]
        for food in foods:
            if food not in resume_orders_food:
                resume_orders_food[food] = foods.count(food)
        return resume_orders_food

    def orders_by_day(self):
        resume_orders_day = {}
        days = [order[2] for order in self.orders]
        for day in days:
            if day not in resume_orders_day:
                resume_orders_day[day] = days.count(day)
        return resume_orders_day

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = self.resume_orders_food_customer(costumer)
        return max(orders, key=orders.get)

    def get_never_ordered_per_costumer(self, costumer):
        orders = set(list(self.resume_orders_food_customer(costumer)))
        orders_set = set([order[1] for order in self.orders])
        return orders_set.difference(orders)

    def get_days_never_visited_per_costumer(self, costumer):
        days_set = set([order[2] for order in self.orders])
        days = [
            order[2] for order in self.orders if order[0] == costumer
        ]
        requested_days_set = set(days)
        return days_set.difference(requested_days_set)

    def get_busiest_day(self):
        days_dict = self.orders_by_day()
        return max(days_dict, key=days_dict.get)

    def get_least_busy_day(self):
        days_dict = self.orders_by_day()
        return min(days_dict, key=days_dict.get)
