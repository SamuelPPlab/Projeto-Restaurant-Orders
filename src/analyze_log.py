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


def get_dish_type(orders_list):
    dishes_type = {order["order"] for order in orders_list}
    return dishes_type


# src: https://www.w3schools.com/python/ref_set_symmetric_difference.asp
def get_never_ordered(customer_name, orders_list):
    dishes_type = get_dish_type(orders_list)
    customer_orders = get_customer_orders(customer_name, orders_list)
    never_ordered = dishes_type.symmetric_difference(customer_orders)
    return never_ordered

def analyze_log(path_to_file):
    orders_data = open_csv(path_to_file)
    customer_maria_data = get_most_ordered_by_customer("maria", orders_data)
    customer_arnaldo_data = get_howmany_customer_has_ordered(
        "arnaldo", "hamburguer", orders_data
    )
    customer_joao_data_dish = get_never_ordered("joao", orders_data)
    print(customer_joao_data_dish)
    return customer_arnaldo_data
