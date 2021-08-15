import csv


def read_file_csv(path_to_file):
    with open(path_to_file) as file:
        keys = ["name", "order", "day"]  # @vanessaberbidi
        list_data = []
        file_reader = csv.DictReader(file, delimiter=",", fieldnames=keys)
        for line in file_reader:
            list_data.append(line)
    return list_data


def most_request_food(client_requests):
    most_repeated_foods = dict()
    most_repeated = None

    for food in client_requests:
        if food in most_repeated_foods:
            most_repeated_foods[food] += 1
        else:
            most_repeated_foods[food] = 1

        if (
            not most_repeated
            or most_repeated_foods[most_repeated] < most_repeated_foods[food]
        ):
            most_repeated = food

    return most_repeated


def client_fav_dish(path_to_file, name):
    list_data = read_file_csv(path_to_file)
    client_orders = []
    for line in list_data:
        if line["name"] == name:
            client_orders.append(line["order"])
    # print(client_orders)
    return most_request_food(client_orders)


def order_quantity(path_to_file, name, order):
    list_data = read_file_csv(path_to_file)
    counter = 0
    for item in list_data:
        if item["name"] == name and item["order"] == order:
            counter += 1
    return counter


def client_never_asked_dishes(path_to_file, name):
    list_data = read_file_csv(path_to_file)
    menu = set()
    client_orders = set()
    for item in list_data:
        menu.add(item["order"])

    for item in list_data:
        if item["name"] == name:
            client_orders.add(item["order"])

    return menu.difference(client_orders)


def days_client_did_not_show_up(path_to_file, name):
    list_data = read_file_csv(path_to_file)
    week_days = set()
    client_visit_days = set()
    for item in list_data:
        week_days.add(item["day"])

    for item in list_data:
        if item["name"] == name:
            client_visit_days.add(item["day"])

    return week_days.difference(client_visit_days)


def analyze_log(path_to_file):
    data_list = []
    with open("data/mkt_campaign.txt", mode="w"):
        data_list.append(client_fav_dish(path_to_file, "maria"))
        data_list.append(
            order_quantity("data/orders_1.csv", "arnaldo", "hamburguer")
        )
        data_list.append(
            client_never_asked_dishes("data/orders_1.csv", "joao")
        )
        data_list.append(
            days_client_did_not_show_up("data/orders_1.csv", "joao")
        )
    print("test", data_list)
    return create_file("data/mkt_campaign.txt", data_list)


def create_file(path, list_data):
    with open(path, "w") as restaurant_data:
        for line in list_data:
            items = [f"{line}\n"]  # @samantabelow
            restaurant_data.writelines(items)
