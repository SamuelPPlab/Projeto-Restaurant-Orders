import csv
from collections import Counter


def get_csv_data(path):
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path}'")

    data = csv.DictReader(open(path), fieldnames=["name", "order", "day"])
    return [row for row in data]


def favorite_food(name, data):
    customer_orders = [
        customer["order"] for customer in data if customer["name"] == name
    ]
    return Counter(customer_orders).most_common(1)[0][0]


def repeated_orders(name, meal, data):
    customer_order = [
        customer["order"] for customer in data if customer["name"] == name
    ]
    return Counter(customer_order).get(meal)


def never_ordered(name, data):
    orders = {customer["order"] for customer in data}
    orders_per_customer = {
        customer["order"] for customer in data if customer["name"] == name
    }
    return orders.symmetric_difference(orders_per_customer)


def no_record(name, data):
    order_days = {customer["day"] for customer in data}
    days_customer = {
        customer["day"] for customer in data if customer["name"] == name
    }
    return order_days.symmetric_difference(days_customer)


def analyze_log(path_to_file):
    data = get_csv_data(path_to_file)

    fav = favorite_food("maria", data)
    repeated = repeated_orders("arnaldo", "hamburguer", data)
    non_ord = never_ordered("joao", data)
    days = no_record("joao", data)

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(f"{fav}\n{repeated}\n{non_ord}\n{days}")
