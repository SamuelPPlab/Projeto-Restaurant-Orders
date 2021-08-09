import csv


class CustomerOrders:
    def __init__(self, name, orders):
        self._name = name
        self._orders = self.extract_orders(orders)

    def extract_orders(self, orders):
        extracted_orders = []
        for person, order, day in orders:
            if person == self._name:
                extracted_orders.append([order, day])
            else:
                continue
        return extracted_orders

    def get_orders(self):
        return self._orders

    def product_total_orders(self, product_name):
        product_total = 0
        for product, _day in self._orders:
            if product == product_name:
                product_total += 1
            else:
                continue

        return product_total

    def most_ordered_dish(self):
        most_ordered = {}
        for product, _day in self._orders:
            most_ordered[product] = most_ordered.get(product, 0) + 1
        return max(most_ordered, key=most_ordered.get)

    def never_ordered_dish(self, menu):
        ordered_dishes = {order[0] for order in self._orders}
        return menu - ordered_dishes

    def days_never_visited(self, work_days):
        visited_days = {order[1] for order in self._orders}
        return work_days - visited_days


class Restaurant:
    def __init__(self, orders):
        self._products = {item[1] for item in orders}
        self._work_days = {item[2] for item in orders}

    def get_menu(self):
        return self._products

    def get_work_days(self):
        return self._work_days


def write_csv_to_file(path_to_file, analyzed_log):
    with open(path_to_file, "w") as file:
        for order in analyzed_log:
            file.write("{0}\n".format(order))


def extract_file_content(path_to_file):
    with open(path_to_file) as file:
        return list(csv.reader(file))


def analyze_log(path_to_file):
    analyzed_log = []
    orders = extract_file_content(path_to_file)

    restaurant = Restaurant(orders)

    arnaldo_orders = CustomerOrders("arnaldo", orders)
    maria_orders = CustomerOrders("maria", orders)
    joao_orders = CustomerOrders("joao", orders)

    marias_most_ordered_dish = maria_orders.most_ordered_dish()
    arnaldos_hamburguer_total = arnaldo_orders.product_total_orders(
        "hamburguer"
    )
    joao_nevers_ordered = joao_orders.never_ordered_dish(restaurant.get_menu())
    joao_nevers_went_on = joao_orders.days_never_visited(
        restaurant.get_work_days()
    )

    analyzed_log.append(marias_most_ordered_dish)
    analyzed_log.append(arnaldos_hamburguer_total)
    analyzed_log.append(joao_nevers_ordered)
    analyzed_log.append(joao_nevers_went_on)

    file_to_write = "data/mkt_campaign.txt"
    write_csv_to_file(file_to_write, analyzed_log)


if __name__ == "__main__":
    orders_log_path = "../data/orders_1.csv"
    analyze_log(orders_log_path)
