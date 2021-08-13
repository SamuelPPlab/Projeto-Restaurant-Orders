class TrackOrders:
    orders = {}
    menu = set()
    days = set()
    visited_days = {}
    size = 0

    def __len__(self):
        return self.size

    def add_visited_day(self, day):
        if day not in self.visited_days:
            self.visited_days[day] = 1
        else:
            self.visited_days[day] += 1

    def add_new_order(self, costumer, order, day):
        self.size += 1

        if costumer not in self.orders:
            self.orders[costumer] = {
                'dishes': {
                    order: 1
                },
                'day': {day}
            }
        elif order in self.orders[costumer]['dishes']:
            self.orders[costumer]['dishes'][order] += 1
            self.orders[costumer]['day'] = (
                self.orders[costumer]['day'].union({day})
            )
        else:
            self.orders[costumer]['dishes'][order] = 1
            self.orders[costumer]['day'] = (
                self.orders[costumer]['day'].union({day})
            )

        self.add_visited_day(day)
        self.menu = self.menu.union({order})
        self.days = self.days.union({day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        dish = ''
        bigger_number = 0

        for order_name, quantity in self.orders[costumer]['dishes'].items():
            if quantity > bigger_number:
                dish = order_name
                bigger_number = quantity

        return dish

    def get_never_ordered_per_costumer(self, costumer):
        return self.menu.difference(
            set(self.orders[costumer]['dishes'].keys())
        )

    def get_days_never_visited_per_costumer(self, costumer):
        return self.days.difference(self.orders[costumer]['day'])

    def get_busiest_day(self):
        busiest_day = ''
        biggest_visited_number = 0

        for day, visits in self.visited_days.items():
            if visits > biggest_visited_number:
                busiest_day = day
                biggest_visited_number = visits

        return busiest_day

    def get_least_busy_day(self):
        least_busy_day = list(self.visited_days.keys())[0]
        least_visited_number = list(self.visited_days.values())[0]

        for day, visits in self.visited_days.items():
            if visits < least_visited_number:
                least_busy_day = day
                least_visited_number = visits

        return least_busy_day
