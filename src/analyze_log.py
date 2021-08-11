import csv
from collections import Counter


def open_csv(path_to_file):
    with open(path_to_file) as c_file:
        file_keys = ["name", "order", "day"]
        file = csv.DictReader(c_file, fieldnames=file_keys)
        orders = []
        for line in file:
            orders.append(line)
        return orders


def get_customer_orders(customer_name, orders_list):
    customer_orders = []
    for order in orders_list:
        if order["name"] == customer_name:
            customer_orders.append(order["order"])
    counter = Counter(customer_orders)
    return counter


def get_most_ordered_by_customer(customer_name, orders_list):
    counter = get_customer_orders(customer_name, orders_list)
    most_frequent = max(counter)
    return most_frequent


def get_howmany_customer_has_ordered(customer_name, order, orders_list):
    counter = get_customer_orders(customer_name, orders_list)
    order_count = counter.get(order)
    return order_count


def analyze_log(path_to_file):
    orders_data = open_csv(path_to_file)
    customer_maria_data = get_most_ordered_by_customer("maria", orders_data)
    customer_arnaldo_data = get_howmany_customer_has_ordered(
        "arnaldo", "hamburguer", orders_data
    )
    print(customer_arnaldo_data)
    return customer_arnaldo_data
