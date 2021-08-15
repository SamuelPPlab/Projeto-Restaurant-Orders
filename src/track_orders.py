class TrackOrders:
    def __init__(self):
        self.stock = []

    def __len__(self):
        return len(self.stock)

    def add_new_order(self, costumer, order, day):
        self.stock.append([costumer, order, day])

    def get_data(self, costumer, type_data):
        person_data = {}
        others_data = {}
        index = 1
        if type_data == "days":
            index = 2
        for data in self.stock:
            if data[0] == costumer:
                set_data = set(person_data)
                person_data = set_data.union({data[index]})
            elif data[index] not in others_data:
                others_data[data[index]] = 1
            else:
                others_data[data[index]] += 1
        others_data = set(others_data)
        return person_data ^ others_data

    def get_day(self):
        days = {}
        result = None
        for data in self.stock:
            if data[2] not in days:
                days[data[2]] = 1
            else:
                days[data[2]] += 1
        if len(days) > 0:
            result = sorted(days, key=days.get, reverse=True)
        return result

    def get_most_ordered_dish_per_costumer(self, costumer):
        foods = {}
        result = None
        for people in self.stock:
            if people[0] == costumer:
                if people[1] not in foods:
                    foods[people[1]] = 1
                else:
                    foods[people[1]] += 1
        if len(foods) > 0:
            result = sorted(foods, key=foods.get, reverse=True)[0]
        return result

    def get_order_frequency_per_costumer(self, costumer, order):
        count_food = {}
        for people in self.stock:
            if people[0] == costumer and people[1] == order:
                if people[0] not in count_food:
                    count_food[order] = 1
                else:
                    count_food[order] += 1
        if len(count_food) == 0:
            return 0
        return count_food[order]

    def get_never_ordered_per_costumer(self, costumer):
        return self.get_data(costumer, "order")

    def get_days_never_visited_per_costumer(self, costumer):
        return self.get_data(costumer, "days")

    def get_busiest_day(self):
        return self.get_day().pop(0)

    def get_least_busy_day(self):
        return self.get_day().pop()

# ins = TrackOrders()
# # # assert len(ins) == 0
# print(ins.get_busiest_day())
