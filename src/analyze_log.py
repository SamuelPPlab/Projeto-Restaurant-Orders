import csv


def parse_csv(path_to_file):
    with open(path_to_file) as file:
        reader = csv.DictReader(file, ["Nome", "Pedido", "Dia"])
        data = list(line for line in reader)
    return data


def get_orders_for_client(lista, name):
    counter = {}
    for item in lista:
        if item["Nome"] == name:
            if item["Pedido"] not in counter:
                counter[item["Pedido"]] = 0
            counter[item["Pedido"]] += 1
    return counter


def get_max_value_in_dict(dict_):
    return max(zip(dict_.values(), dict_.keys()))[1]


def get_quantity_order_by_client(lista, name, order):
    quantity_order = 0
    for item in lista:
        if item["Nome"] == name and item["Pedido"] == order:
            quantity_order += 1
    return quantity_order


def get_all_order_options(lista):
    all_orders = []
    for item in lista:
        all_orders.append(item["Pedido"])
    return set(all_orders)


def get_all_days(lista):
    all_days = []
    for item in lista:
        all_days.append(item["Dia"])
    return set(all_days)


def get_order_never_request(lista, name):
    orders = []
    for item in lista:
        if item["Nome"] == name:
            orders.append(item["Pedido"])
    order_not_requested = set(orders)
    all_menu = get_all_order_options(lista)
    result = all_menu.difference(order_not_requested)
    return result


def get_days_not_visited(lista, name):
    days = []
    for item in lista:
        if item["Nome"] == name:
            days.append(item["Dia"])
    days_visited = set(days)

    all_days = get_all_days(lista)

    return all_days.difference(days_visited)


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        reader = csv.DictReader(file, ["Nome", "Pedido", "Dia"])
        data = list(line for line in reader)

        report = [
            f"{get_max_value_in_dict(get_orders_for_client(data, 'maria'))}\n"
            f"{get_quantity_order_by_client(data, 'arnaldo', 'hamburguer')}\n"
            f"{get_order_never_request(data, 'joao')}\n"
            f"{get_days_not_visited(data, 'joao')}"
        ]

    with open("data/mkt_campaign.txt", "w") as file:
        file.writelines(report)
