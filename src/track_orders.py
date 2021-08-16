from collections import Counter


class TrackOrders:
    def __init__(self):
        self.wish_list = []

    def __len__(self):
        return len(self.wish_list)

    def add_new_order(self, costumer, order, day):
        self.wish_list.append({
            "name_client": costumer, "dishes": order, "days": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        ordered_dishes = [
            request["dishes"]
            for request in self.wish_list
            if request["name_client"] == costumer
        ]
        count = Counter(ordered_dishes)
        most_requested_dishes = count.most_common(1)[0][0]
        return most_requested_dishes

    def get_never_ordered_per_costumer(self, costumer):
        every_dish = {request["dishes"] for request in self.wish_list}
        ordered_dishes = {
            request["dishes"]
            for request in self.wish_list
            if request["name_client"] == costumer
        }
        ordered_not_dishes = every_dish.symmetric_difference(
                                ordered_dishes)
        return ordered_not_dishes

    def get_days_never_visited_per_costumer(self, costumer):
        every_day = {request["days"] for request in self.wish_list}
        days_go = {
            request["days"]
            for request in self.wish_list
            if request["name_client"] == costumer
        }
        days_not_go = every_day.symmetric_difference(
                        days_go)
        return days_not_go

    def get_busiest_day(self):
        days_go = [
            request["days"]
            for request in self.wish_list
        ]

        count = Counter(days_go)
        days_more = max(count, key=count.get)
        return days_more

    def get_least_busy_day(self):
        days_go = [
            request["days"]
            for request in self.wish_list
        ]

        count = Counter(days_go)
        days_less = min(count, key=count.get)
        return days_less

    def get_dish_quantity_per_costumer(self, costumer, order):
        ordered_dishes = [
            request["dishes"]
            for request in self.wish_list
            if request["name_client"] == costumer
        ]
        count = Counter(ordered_dishes)
        demanded = count.get(order)
        return demanded
