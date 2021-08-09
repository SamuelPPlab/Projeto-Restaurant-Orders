from inventory_control import InventoryControl


class TrackOrders:
    def __init__(self):
        self.orders = {}

    def __len__(self):
        pass

    def add_new_order(self, costumer, order, day):
        if costumer in self.orders:
            if order in self.orders[costumer]["dishes"]:
                self.orders[costumer]["dishes"][order] += 1
            else:
                self.orders[costumer]["dishes"][order] = 1
            if day in self.orders[costumer]["days"]:
                self.orders[costumer]["days"][day] += 1
            else:
                self.orders[costumer]["days"][day] = 1
        else:
            self.orders[costumer] = {"dishes": {order: 1}, "days": {day: 1}}

    def get_most_ordered_dish_per_costumer(self, costumer):
        return max(
            self.orders[costumer]["dishes"],
            key=self.orders[costumer]["dishes"].get,
        )

    def get_never_ordered_per_costumer(self, costumer):
        return set(InventoryControl.INGREDIENTS.keys()).difference(
            self.orders[costumer]["dishes"].keys()
        )

    def get_days_never_visited_per_costumer(self, costumer):
        return set(
            [
                "segunda-feira",
                "terça-feira",
                "quarta-feira",
                "quinta-feira",
                "sexta-feira",
                "sabado",
                "domingo",
            ]
        ).difference(self.orders[costumer]["days"].keys())

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
