class TrackOrders:
    def __init__(self):
        self.orders = []
        self.people = set()
        self.foods = set()
        self.days = set()
        self.person_foods = dict()
        self.person_days = dict()
        self.days_count = dict()

    def __len__(self):
        return len(self.orders)

    def populate_person_foods(self, person, food):
        if person not in self.person_foods:
            self.person_foods[person] = {}

        if food not in self.person_foods[person]:
            self.person_foods[person][food] = 1
        else:
            self.person_foods[person][food] += 1

    def populate_person_days(self, person, day):
        if person not in self.person_days:
            self.person_days[person] = {}

        if day not in self.person_days[person]:
            self.person_days[person][day] = 1
        else:
            self.person_days[person][day] += 1

    def populate_days_count(self, day):
        if day not in self.days_count:
            self.days_count[day] = 1
        else:
            self.days_count[day] += 1

    def populate_lists(self, person, food, day):
        self.people.add(person)
        self.foods.add(food)
        self.days.add(day)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))
        self.populate_lists(customer, order, day)
        self.populate_person_foods(customer, order)
        self.populate_person_days(customer, day)
        self.populate_days_count(day)

    def get_most_ordered_dish_per_costumer(self, customer):
        bigger_quantity = 0
        most_ordered = ""

        for order, quantity in self.person_foods[customer].items():
            if quantity > bigger_quantity:
                bigger_quantity = quantity
                most_ordered = order

        return most_ordered

    def get_never_ordered_per_costumer(self, customer):
        person_orders = set(self.person_foods[customer])

        return self.foods.difference(person_orders)

    def get_dish_quantity_per_costumer(self, customer, order):
        return self.person_foods[customer][order]

    def get_days_never_visited_per_costumer(self, customer):
        person_frequency = set(self.person_days[customer])

        return self.days.difference(person_frequency)

    def get_quantities_to_buy(self):
        pass

    def get_busiest_day(self):
        bigger_frequency = 0
        most_frequented = ""

        for day, quantity in self.days_count.items():

            if quantity > bigger_frequency:
                bigger_frequency = quantity
                most_frequented = day

        return most_frequented

    def get_least_busy_day(self):
        smallest_frequency = 1000
        less_frequented = ""

        for day, quantity in self.days_count.items():
            if quantity < smallest_frequency:
                smallest_frequency = quantity
                less_frequented = day

        return less_frequented
