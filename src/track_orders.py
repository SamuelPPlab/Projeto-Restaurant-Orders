def plates(self):
    plates = set()
    for order in self.orders:
        plates.add(order["order"])
    return plates


def wishes_by_costumer(self, costumer):
    food_count = {}
    for order in self.orders:
        client = order["costumer"]
        food = order["order"]
        if client == costumer:
            if food not in food_count:
                food_count[food] = 1
            else:
                food_count[food] += 1
    return food_count


def plates_by_client(self, costumer):
    plates = set()
    for order in self.orders:
        client = order["costumer"]
        if client == costumer:
            plates.add(order["order"])
    return plates


def days_visited_by_client(self, costumer):
    days = set()
    for order in self.orders:
        client = order["costumer"]
        if client == costumer:
            days.add(order["day"])
    return days


def working_days(self):
    days = set()
    for order in self.orders:
        days.add(order["day"])
    return days


def frequency_days(self):
    day_counter = {}
    for order in self.orders:
        day = order["day"]
        if day not in day_counter:
            day_counter[day] = 1
        else:
            day_counter[day] += 1
    return day_counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        food_count = wishes_by_costumer(self, costumer)
        return max(food_count, key=food_count.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        food_count = wishes_by_costumer(self, costumer)
        return food_count[order]

    def get_never_ordered_per_costumer(self, costumer):
        available_plates = plates(self)
        plates_client = plates_by_client(self, costumer)
        return available_plates.difference(plates_client)

    def get_days_never_visited_per_costumer(self, costumer):
        days_opened = working_days(self)
        days_visited = days_visited_by_client(self, costumer)
        return days_opened.difference(days_visited)

    def get_busiest_day(self):
        days_count = frequency_days(self)
        return max(days_count, key=days_count.get)

    def get_least_busy_day(self):
        days_count = frequency_days(self)
        return min(days_count, key=days_count.get)
