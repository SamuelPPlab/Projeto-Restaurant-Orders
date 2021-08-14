from src.utils.most_request_food import most_request_food
from src.utils.best_counter import count


class TrackOrders:
    def __init__(self):
        self.__orders_by_costumer = dict()
        self.__len = 0
        self.__food_menu = set()
        self.__opening_days = set()

    def __len__(self):
        return self.__len

    def add_new_order(self, costumer, order, day):
        if costumer in self.__orders_by_costumer:
            self.__orders_by_costumer[costumer].append((order, day))
        else:
            self.__orders_by_costumer[costumer] = [(order, day)]

        self.__len += 1
        self.__food_menu.add(order)
        self.__opening_days.add(day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return most_request_food(self.__orders_by_costumer[costumer])

    def get_dish_quantity_per_costumer(self, costumer, order):
        return count(
            lambda item: True if order in item else False,
            self.__orders_by_costumer[costumer],
        )

    def get_never_ordered_per_costumer(self, costumer):
        client_foods = {
            food for food, _ in self.__orders_by_costumer[costumer]
        }
        return self.__food_menu.difference(client_foods)

    def get_days_never_visited_per_costumer(self, costumer):
        client_went_to_the_restaurant = {
            day for _, day in self.__orders_by_costumer[costumer]
        }
        return self.__opening_days.difference(client_went_to_the_restaurant)

    def get_busiest_day(self):
        days_for_quantities = dict()
        busiest_day = None
        for client in self.__orders_by_costumer.values():
            for _, day in client:
                if day in days_for_quantities:
                    days_for_quantities[day] += 1
                else:
                    days_for_quantities[day] = 1

                if (
                    not busiest_day
                    or days_for_quantities[day]
                    > days_for_quantities[busiest_day]
                ):
                    busiest_day = day
        return busiest_day

    def get_least_busy_day(self):
        days_for_quantities = dict()
        least_busy_day = None
        for client in self.__orders_by_costumer.values():
            for _, day in client:
                if day in days_for_quantities:
                    days_for_quantities[day] += 1
                else:
                    days_for_quantities[day] = 1

                if (
                    not least_busy_day
                    or days_for_quantities[day]
                    < days_for_quantities[least_busy_day]
                ):
                    least_busy_day = day
        return least_busy_day
