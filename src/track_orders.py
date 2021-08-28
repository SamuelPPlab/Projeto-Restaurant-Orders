class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        plates_count = dict()
        max_order_plate = 0
        favorite_plate = ""
        for order in self.orders:

            # checking if client ordered is equal to costumer
            if order[0] == costumer:

                # checkint if plate are already on plates_count dict
                if order[1] in plates_count:
                    plates_count[order[1]] += 1
                else:
                    plates_count[order[1]] = 1

                # checking if actual plate most requested
                if plates_count[order[1]] > max_order_plate:
                    max_order_plate = plates_count[order[1]]
                    favorite_plate = order[1]
        return favorite_plate

    def get_never_ordered_per_costumer(self, costumer):
        order_client = set()
        all_orders = set()

        # order[1] = plate ordered
        # order[0] = client that make order
        for order in self.orders:
            all_orders.add(order[1])
        for order in self.orders:
            if order[0] == costumer:
                order_client.add(order[1])
        return all_orders.difference(order_client)

    def get_days_never_visited_per_costumer(self, costumer):
        days_with_orders = set()
        all_days = set()

        # order[2] = day of order
        # order[0] = client that make order
        for order in self.orders:
            all_days.add(order[2])
        for order in self.orders:
            if order[0] == costumer:
                days_with_orders.add(order[2])
        return all_days.difference(days_with_orders)

    def get_busiest_day(self):
        days_count_order = dict()
        max_order = 0
        busiest_day = ""
        for order in self.orders:
            if order[2] in days_count_order:
                days_count_order[order[2]] += 1
            else:
                days_count_order[order[2]] = 1

            if days_count_order[order[2]] > max_order:
                max_order = days_count_order[order[2]]
                busiest_day = order[2]
        return busiest_day

    def get_least_busy_day(self):
        days_count_order = dict()
        min_order = 999
        least_busy_day = ""
        for order in self.orders:
            if order[2] in days_count_order:
                days_count_order[order[2]] += 1
            else:
                days_count_order[order[2]] = 1

            if days_count_order[order[2]] <= min_order:
                min_order = days_count_order[order[2]]
                least_busy_day = order[2]
        return least_busy_day
