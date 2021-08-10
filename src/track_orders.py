from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def all_dishes(dish_list):
        all_dishes = []
        for order in dish_list:
            if order[1] not in all_dishes:
                all_dishes.append(order[1])
        return all_dishes

    def get_most_ordered_dish_per_costumer(self, costumer):
        count_dish = {}
        for order in self.orders:
            if order[0] == costumer:
                if order[1] not in count_dish:
                    count_dish[order[1]] = 1
                else:
                    count_dish[order[1]] += 1

        most_ordered = Counter(count_dish).most_common(1)[0][0]
        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        count_dish = {}
        all_ordered_dishes = TrackOrders.all_dishes(self.orders)

        for order in self.orders:
            if order[0] == costumer:
                if order[1] not in count_dish:
                    count_dish[order[1]] = 1
                else:
                    count_dish[order[1]] += 1

        counted_dish = set(count_dish)
        all_ordered = set(all_ordered_dishes)

        return all_ordered.difference(counted_dish)

    def every_day_of_the_week(dish_list):
        all_days = []
        for order in dish_list:
            if order[2] not in all_days:
                all_days.append(order[2])
        return all_days

    def get_days_never_visited_per_costumer(self, costumer):
        days_attended = []

        all_days_of_the_week = TrackOrders.every_day_of_the_week(self.orders)

        for order in self.orders:
            if order[0] == costumer:
                if order[2] not in days_attended:
                    days_attended.append(order[2])

        all_days_csv_file = set(all_days_of_the_week)
        days_attended_by_name = set(days_attended)

        return all_days_csv_file.difference(days_attended_by_name)

    def get_busiest_day(self):
        all_days = [order[2] for order in self.orders]
        busiest_day = Counter(all_days).most_common(1)[0][0]
        return busiest_day

    def get_least_busy_day(self):
        all_days = [order[2] for order in self.orders]
        least_busiest_day = Counter(all_days).most_common()[-1][0]
        return least_busiest_day
