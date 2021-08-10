import csv
from collections import Counter

# from collections import ChainMap


def import_csv(path_to_file):
    if path_to_file.endswith(".csv"):
        with open(path_to_file, mode="r") as csv_file:
            fieldnames = ["customer", "order", "weekday"]
            return list(csv.DictReader(csv_file, fieldnames))

    raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")


def writer_txt(message):
    with open("data/mkt_campaign.txt", "a") as txt_file:
        txt_file.writelines(str(message) + "\n")
        txt_file.close()


def get_most_request_order_by_customer(log, customer):
    orders = []
    for item in log:
        if item["customer"] == customer:
            orders.append(item["order"])
    most_request_order = Counter(orders).most_common(1)
    return (most_request_order[0])[0]


def get_orders_quantity_by_costumer(log, order, customer):
    counter = 0
    for item in log:
        if item["order"] == order and item["customer"] == customer:
            counter += 1
    return counter


def get_order_never_asked_by_customer(log, customer):
    orders_type = set()
    customer_orders = set()
    for item in log:
        orders_type.add(item["order"])
        if item["customer"] == customer:
            customer_orders.add(item["order"])
    return orders_type.difference(customer_orders)


def get_days_never_visited_per_costumer(log, customer):
    weekdays = set()
    customer_weekdays = set()
    for item in log:
        weekdays.add(item["weekday"])
        if item["customer"] == customer:
            customer_weekdays.add(item["weekday"])
    return weekdays.difference(customer_weekdays)


def analyze_log(path_to_file):
    # raise NotImplementedError
    log = import_csv(path_to_file)
    # print(get_most_request_order_by_customer(log, "maria"))
    writer_txt(get_most_request_order_by_customer(log, "maria"))
    # print(get_orders_quantity_by_costumer(log, "hamburguer", "arnaldo"))
    writer_txt(get_orders_quantity_by_costumer(log, "hamburguer", "arnaldo"))
    writer_txt(get_order_never_asked_by_customer(log, "joao"))
    writer_txt(get_days_never_visited_per_costumer(log, "joao"))
    # return


# print(analyze_log("data/orders_1.csv"))
# analyze_log("data/orders_1.csv")
