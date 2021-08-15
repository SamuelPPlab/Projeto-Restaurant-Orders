from src.customer import Costumer


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        costumer_in_orders = self.getCostumer(costumer)
        if costumer_in_orders is not None:
            costumer_in_orders.add_new_order(order)
            return costumer_in_orders.add_new_day(day)
        return self.orders.append(Costumer(costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        return self.getCostumer(costumer).most_ordered_dish()

    def get_dish_quantity_per_costumer(self, costumer, order):
        return self.getCostumer(costumer).get_dish_quantity(order)

    def get_never_ordered_per_costumer(self, costumer):
        all_dishs = self.generate_all_dishs()
        print(all_dishs)
        customer_orders = set(self.getCostumer(costumer).order)
        return all_dishs.symmetric_difference(customer_orders)

    def get_busiest_day(self):
        presence_list = self.generate_presence_list()
        return max(set(presence_list), key=presence_list.count)

    def get_least_busy_day(self):
        presence_list = self.generate_presence_list()
        return min(set(presence_list), key=presence_list.count)

    def get_days_never_visited_per_costumer(self, customer):
        presence_list = set(self.generate_presence_list())
        user_presence_list = set(self.getCostumer(customer).day)
        return presence_list.symmetric_difference(user_presence_list)

    def getCostumer(self, costumer):
        customer_list = list(filter(lambda x: x.name == costumer, self.orders))
        if len(customer_list) != 0:
            return customer_list[0]
        return None

    def generate_all_dishs(self):
        dishs = []
        for i in self.orders:
            dishs = dishs + i.order
        return set(dishs)

    def generate_presence_list(self):
        days = []
        for i in self.orders:
            days = days + i.day
        return days
