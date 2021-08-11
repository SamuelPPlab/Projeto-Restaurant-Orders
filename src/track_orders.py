class TrackOrders:
    def __len__(self):
        return len(self.orders)
    
    def __init__(self):
        self.orders = []

    def add_new_order(self, costumer, order, day):
        self.orders.append({'name': costumer, 'order':order, 'day':day })
        return self.orders

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_ordered = []
        for item in self.orders:
            if item['name'] == costumer:
                most_ordered.append(item['order'])
        return max(set(most_ordered), key=most_ordered.count)

    def get_never_ordered_per_costumer(self, costumer):
        ordered = []
        dish_ordered = []
        for item in self.orders:
            if item['name'] == costumer:
                dish_ordered.append(item['order'])
            ordered.append(item['order'])
            never_ordered = {item for item in ordered if item not in dish_ordered}
            return never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
