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
    most_frequent = counter.most_common(1)[0][0]
    print(most_frequent)
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


def get_visited_day(orders_list):
    days = {order["day"] for order in orders_list}
    return days


def get_customer_day_visited(customer_name, orders_list):
    days = {
        order["day"]
        for order in orders_list
        if order["name"] == customer_name
    }
    return days


def get_never_visited_day(customer_name, orders_list):
    days = get_visited_day(orders_list)
    customer_orders = get_customer_day_visited(customer_name, orders_list)
    never_visited = days.symmetric_difference(customer_orders)
    return never_visited


def validate_extension(path_to_file):
    extension_file = path_to_file.split('.').pop()
    if extension_file != "csv":
        raise FileNotFoundError(
            f"No such file or directory: '{path_to_file}'"
        )


def analyze_log(path_to_file):
    validate_extension(path_to_file)
    file = "data/mkt_campaign.txt"
    orders_data = open_csv(path_to_file)
    customer_maria_data = get_most_ordered_by_customer("maria", orders_data)
    customer_arnaldo_data = get_howmany_customer_has_ordered(
        "arnaldo", "hamburguer", orders_data
    )
    customer_joao_data_dish = get_never_ordered("joao", orders_data)
    customer_joao_data_day = get_never_visited_day("joao", orders_data)
    data = [
        f"{customer_maria_data}\n",
        f"{customer_arnaldo_data}\n",
        f"{customer_joao_data_dish}\n",
        f"{customer_joao_data_day}\n",
    ]
    with open(file, "w") as f:
        f.writelines(data)
