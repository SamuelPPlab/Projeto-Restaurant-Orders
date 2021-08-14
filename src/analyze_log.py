import csv


def more_requests_maria(data_orders):
    orders = []
    maxi = set()
    for item in data_orders:
        if item[0] == "maria":
            orders.append(item[1])
    for order in orders:
        maxi.add((orders.count(order), order))
        maxi_plus = dict(maxi)
    return maxi_plus[max(maxi_plus)]


def more_requests_arnaldo(data_orders):
    orders = []
    for item in data_orders:
        if item[0] == "arnaldo":
            orders.append(item[1])
    return orders.count("hamburguer")


def more_requests_never_asked_joao(data_orders):
    orders = set()
    ordered = set()
    for item in data_orders:
        if item[0] == "joao":
            ordered.add(item[1])
        else:
            orders.add(item[1])
    return orders - ordered


def joao_visited(data_days):
    days = set()
    joao_days = set()
    for item in data_days:
        if item[0] == "joao":
            joao_days.add(item[2])
        else:
            days.add(item[2])
    return days - joao_days


def import_data(path):
    try:
        list_data = []
        with open(path) as file:
            reader = csv.reader(file, delimiter="\n")
            for item in reader:
                refact = item[0].split(",")
                list_data.append(refact)
            return list_data
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: '{path}'")


def analyze_log(path):
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path}'")

    data = import_data(path)
    maria_requests = more_requests_maria(data)
    arnaldo_requests = more_requests_arnaldo(data)
    joao_requests = more_requests_never_asked_joao(data)
    visited = joao_visited(data)

    txt = open("data/mkt_campaign.txt", "w")
    txt.write(
        f"{maria_requests}\n{arnaldo_requests}\n{joao_requests}\n{visited}"
    )
    txt.close()
    return True
