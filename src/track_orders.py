class TrackOrders:
    def __init__(self):
        self.data = {
            "allDays": {
                "segunda-feira": 0,
                "terça-feira": 0,
                "quarta-feira": 0,
                "quinta-feira": 0,
                "sexta-feira": 0,
                "sabado": 0,
                "sábado": 0,
                "domingo": 0,
            }
        }
        self.allOrders = []

    def __len__(self):
        return len(self.allOrders)

    def add_new_order(self, costumer, order, day):
        if costumer not in self.data:
            self.data[costumer] = {
                "foods": {},
                "dayList": {},
            }
        if order not in self.data[costumer]["foods"]:
            self.data[costumer]["foods"][order] = 1
        else:
            self.data[costumer]["foods"][order] += 1
        if day not in self.data[costumer]["dayList"]:
            self.data[costumer]["dayList"][order] = 1
        else:
            self.data[costumer]["dayList"][order] += 1
        self.data["allDays"][day] += 1
        self.allOrders.append(order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return max(
            self.data[costumer]["foods"],
            key=self.data[costumer]["foods"].get,
        )

    def get_never_ordered_per_costumer(self, costumer):
        ordersSet = set(self.allOrders)
        clientSet = set(
            [
                key
                for key in self.data[costumer]["foods"]
                if self.data[costumer]["foods"][key] != 0
            ]
        )
        return ordersSet.difference(clientSet)

    def get_days_never_visited_per_costumer(self, costumer):
        return {
            key
            for key in self.data[costumer]["dayList"]
            if self.data[costumer]["dayList"][key] == 0
        }

    def get_busiest_day(self):
        return max(
            self.data["allDays"],
            key=self.data["allDays"].get,
        )

    def get_least_busy_day(self):
        return min(
            self.data["allDays"],
            key=self.data["allDays"].get,
        )
