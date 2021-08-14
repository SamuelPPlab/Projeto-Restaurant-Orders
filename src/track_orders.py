class TrackOrders:
    def __init__(self):
        self.orders = []
        self.meals = set()
        self.days = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.meals.add(order)
        self.days.add(day)
        self.orders.append({
            "costumer": costumer,
            "order": order,
            "day": day,
            })

    def get_list_of_meals(self, costumer):
        list_meals = []
        for order in self.orders:
            if order["costumer"] == costumer:
                list_meals.append(order["order"])
        return list_meals

    def get_list_of_days(self, costumer):
        list_days = set()
        for order in self.orders:
            if order["costumer"] == costumer:
                list_days.add(order["day"])
        return list_days

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = {}
        list_meals = self.get_list_of_meals(costumer)

        most_ordered = list_meals[0]

        for meal in list_meals:
            if meal not in count:
                count[meal] = 1
            else:
                count[meal] += 1
            if count[meal] > count[most_ordered]:
                most_ordered = meal
        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        meals_costumer = self.get_list_of_meals(costumer)
        never_ordered = self.meals.difference(set(meals_costumer))

        return never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        list_days = self.get_list_of_days(costumer)

        never_visited = self.days.difference(list_days)

        return never_visited

    def get_busiest_day(self):
        count = {}
        list_days = [order["day"] for order in self.orders]
        most_frequent = list_days[0]
        for day in list_days:
            if day not in count:
                count[day] = 1
            else:
                count[day] += 1
            if count[day] > count[most_frequent]:
                most_frequent = day
        return most_frequent

    def get_least_busy_day(self):
        count = {}
        list_days = [order["day"] for order in self.orders]
        less_frequent = list_days[0]
        for day in list_days:
            if day not in count:
                count[day] = 1
            else:
                count[day] += 1
            if count[day] < count[less_frequent]:
                less_frequent = day
        return less_frequent
