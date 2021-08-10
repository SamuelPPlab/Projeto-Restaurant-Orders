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
    clientOrders = dict()
    for order in orders:
        if order["client"] == client:
            if order["order"] not in clientOrders:
                clientOrders[order["order"]] = 1
            else:
                clientOrders[order["order"]] += 1
    maxValueOrder = max(value for key, value in clientOrders.items())
    product = [
        key
        for key, value in clientOrders.items()
        if clientOrders[key] == maxValueOrder
    ][0]
    return product


def get_number_of_orders_by_client_and_product(path_to_file, client, product):
    orders = read_csv(path_to_file)
    times = 0
    for order in orders:
        if order["client"] == client and order["order"] == product:
            times += 1
    return times


def get_all_products(path_to_file):
    orders = read_csv(path_to_file)
    allProducts = set()
    for order in orders:
        allProducts.add(order["order"])
    return allProducts


def get_never_ordered_by_client(path_to_file, client):
    orders = read_csv(path_to_file)
    productsOrderByClient = [
        order["order"] for order in orders if order["client"] == client
    ]
    allProducts = get_all_products(path_to_file)
    return allProducts.difference(set(productsOrderByClient))


def get_days_off_by_client(path_to_file, client):
    orders = read_csv(path_to_file)
    allDays = set([order["day"] for order in orders])
    daysOn = set(
        [order["day"] for order in orders if order["client"] == client]
    )
    daysOff = allDays.difference(daysOn)
    return daysOff


def analyze_log(path_to_file):
    with open("data/mkt_campaign.txt", "w") as file:
        orderByMaria = get_most_common_order_by_client(
            path_to_file, "maria"
        )

        orderByArnaldo = (
            get_number_of_orders_by_client_and_product(
                path_to_file, "arnaldo", "hamburguer"
            )
        )
        neverOrderByJoao = get_never_ordered_by_client(
            path_to_file, "joao"
        )

        daysOffJoao = get_days_off_by_client(path_to_file, "joao")

        LINES = [
            f"{orderByMaria}\n",
            f"{orderByArnaldo}\n",
            f"{neverOrderByJoao}\n",
            f"{daysOffJoao}\n",
        ]
        file.writelines(LINES)
