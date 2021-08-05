import csv


class BurguerShop:
    def __init__(self, name, orders):
        self.name = name
        self.orders = orders
    
    def get_orders(self, orders):
        orders_fetched = []
        for client, order, pay in orders:
            if client == self.name:
                orders_fetched.append([order, pay])
            else:
                continue
            return orders_fetched
    
    def orders(self):
        return self._orders
    
    def orders_by_products(self, product_name):
        product_by_sale = 0
        for product, _day in self.orders:
            if product == product_name:
                product_by_sale += 1
            else:
                continue
            return product_by_sale
    
    def buyest_dish(self):
        dearest_product = {}
        for product, day in self.orders:
            dearest_product[product] = dearest_product.get(product, 0) + 1
        return max(dearest_product, key=dearest_product.get)
    
    def less_wanted_dish(self, menu):
        ordered_dishes = {order[1] for order in self.orders}
        return menu - ordered_dishes
    
    def poorest_days(self, work_days):
        visited_days = {order[1] for order in self.orders}
        return work_days - visited_days
    

class shop:
    def __init__(self, orders):
        self.products = {order[1] for order in self.orders}
        self.workdays = {order[2] for order in self.orders}
    
    def get_menu(self):
        return self._products
    
    def get_work_days(self):
        return self._work_days


def write_csv_file(path_to_file, analyzed_logs):
    with open(path_to_file, "w") as file:
        for order in analyzed_logs:
            file.write("{0}\n".format(order))


def extract_file(path_to_file):
    with open(path_to_file) as file:
        return list(csv.reader(file))


def analyze_log(path_to_file):
    analyzed_log = []
    orders = extract_file(path_to_file)

    restaurant = shop(orders)

    arnaldo_orders = BurguerShop("arnaldo", orders)
    maria_orders = BurguerShop("maria", orders)
    joao_orders = BurguerShop("joao", orders)

    marias_buyest_dish = maria_orders.buyest_dish()
    arnaldos_buyest_dish = arnaldo_orders.buyest_dish("hamburguer")
    joao_never_ordered = joao_orders.less_wanted_dish(restaurant.get_menu())
    joao_never_went = joao_orders.poorest_days(
        restaurant.get_work_days()
    )

    analyzed_log.append(marias_buyest_dish)
    analyzed_log.append(arnaldos_buyest_dish)
    analyzed_log.append(joao_never_ordered)
    analyzed_log.append(joao_never_went)

    file_to_write = "data/mkt_campaign.txt"
    write_csv_file(file_to_write, analyzed_log)


if __name__ == "__main__":
    orders_path = "../data/orders_1.csv"
    analyze_log(orders_path)
