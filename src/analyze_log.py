import csv
from collections import Counter


def most_frequent_order(client_name, customers_list):
    customer_orders = [
        order["product"]
        for order in customers_list
        if order["client"] == client_name
    ]
    count_orders = Counter(customer_orders)
    most_frequent = count_orders.most_common(1)[0][0]
    return most_frequent


def count_client_order(client_name, product, customers_list):
    customer_orders = [
        order["product"]
        for order in customers_list
        if order["client"] == client_name
    ]
    count_orders = Counter(customer_orders)
    return count_orders[product]


def products_client_not_ordered(client, customers_list):
    menu_from_orders = {order["product"] for order in customers_list}
    client_products_ordered = {
        order["product"]
        for order in customers_list
        if order["client"] == client
    }
    return menu_from_orders.difference(client_products_ordered)


def weekdays_client_not_ordered(client, customers_list):
    weekdays_from_orders = {order["weekday"] for order in customers_list}
    client_weekdays_ordered = {
        order["weekday"]
        for order in customers_list
        if order["client"] == client
    }
    return weekdays_from_orders.difference(client_weekdays_ordered)


def analyze_log(path_to_file):
    try:
        if not path_to_file.endswith("csv"):
            raise ValueError
    except Exception:
        message = f"No such file or directory: '{path_to_file}'"
        raise FileNotFoundError(message)

    with open("data/mkt_campaign.txt", "w") as output:
        output.write("")

    customers_list = []
    with open(path_to_file, "r", newline="") as csvfile:
        FIELDNAMES = ["client", "product", "weekday"]
        CSV_DICT = csv.DictReader(
            csvfile, fieldnames=FIELDNAMES, delimiter=","
        )
        customers_list = [row for row in CSV_DICT]
    maria_most_frequent = most_frequent_order("maria", customers_list)
    arnaldo_hamburguer_orders = count_client_order(
        "arnaldo", "hamburguer", customers_list
    )
    joao_products_not_ordered = products_client_not_ordered(
        "joao", customers_list
    )
    joao_weekdays_not_ordered = weekdays_client_not_ordered(
        "joao", customers_list
    )

    with open("data/mkt_campaign.txt", "a") as output:
        list = [
            f"{maria_most_frequent}\n",
            f"{arnaldo_hamburguer_orders}\n",
            f"{joao_products_not_ordered}\n",
            f"{joao_weekdays_not_ordered}\n",
        ]
        output.writelines(list)
