import csv


def read_csv(path_to_file):
    with open(path_to_file) as file:
        order_reader = csv.reader(file, delimiter=",", quotechar='"')
        list_data = []
        value = dict()
        for line in order_reader:
            value["client"] = line[0]
            value["order"] = line[1]
            value["day"] = line[2]
            list_data.append(value)
            value = {}
    return list_data


def get_most_common_order_by_client(path_to_file, client):
    orders = read_csv(path_to_file)
    client_orders = dict()
    for order in orders:
        if order["client"] == client:
            if order["order"] not in client_orders:
                client_orders[order["order"]] = 1
            else:
                client_orders[order["order"]] += 1
    max_ordered = max(value for key, value in client_orders.items())
    product = [
        key
        for key, value in client_orders.items()
        if client_orders[key] == max_ordered
    ][0]
    return product


def get_number_of_orders_by_client_and_product(path_to_file, client, product):
    orders = read_csv(path_to_file)
    number_of_times = 0
    for order in orders:
        if order["client"] == client and order["order"] == product:
            number_of_times += 1
    return number_of_times


def get_all_products(path_to_file):
    orders = read_csv(path_to_file)
    all_products = set()
    for order in orders:
        all_products.add(order["order"])
    return all_products


def get_never_ordered_by_client(path_to_file, client):
    orders = read_csv(path_to_file)
    ordered_products = [
        order["order"] for order in orders if order["client"] == client
    ]
    all_products = get_all_products(path_to_file)
    return all_products.difference(set(ordered_products))


def get_days_off_by_client(path_to_file, client):
    orders = read_csv(path_to_file)
    all_days = set([order["day"] for order in orders])
    days_on = set(
        [order["day"] for order in orders if order["client"] == client]
    )
    days_off = all_days.difference(days_on)
    return days_off


def analyze_log(path_to_file):
    with open("data/mkt_campaign.txt", "w") as file:
        most_common_order_by_maria = get_most_common_order_by_client(
            path_to_file, "maria"
        )

        times_arnaldo_ordered_hamburguer = (
            get_number_of_orders_by_client_and_product(
                path_to_file, "arnaldo", "hamburguer"
            )
        )
        never_ordered_by_joao = get_never_ordered_by_client(
            path_to_file, "joao"
        )

        days_off_joao = get_days_off_by_client(path_to_file, "joao")

        LINES = [
            f"{most_common_order_by_maria}\n",
            f"{times_arnaldo_ordered_hamburguer}\n",
            f"{never_ordered_by_joao}\n",
            f"{days_off_joao}\n",
        ]
        file.writelines(LINES)
