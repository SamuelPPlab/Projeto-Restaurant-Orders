import csv
from collections import Counter


def read_file(path):
    with open(path) as csvfile:
        keys = ["name", "order", "week_day"]
        reader = csv.DictReader(csvfile, fieldnames=keys)
        data = []
        [data.append(row) for row in reader]
    return data


def get_most_eaten(data, name):
    filter = []
    for item in data:
        if item["name"] == name:
            filter.append(item["order"])
    result = dict(Counter(filter))
    return max(result, key=lambda k: result[k])


def order_number(data, name, order):
    filter = []
    for item in data:
        if item["name"] == name:
            filter.append(item["order"])
    result = dict(Counter(filter))
    return result.get(order)


def order_never_asked(data, name):
    orders = set()
    costumerOrders = set()
    for item in data:
        orders.add(item["order"])
        if item["name"] == name:
            costumerOrders.add(item["order"])
    return orders.difference(costumerOrders)


def days_off(data, name):
    days = set()
    costumerDays = set()
    for item in data:
        days.add(item["week_day"])
        if item["name"] == name:
            costumerDays.add(item["week_day"])
    return days.difference(costumerDays)


def analyze_log(path_to_file):
    if path_to_file.endswith('csv'):
        data = read_file(path_to_file)
        maria_eats = get_most_eaten(data, "maria")
        arnaldo_ask_hamburguer = order_number(data, "arnaldo", "hamburguer")
        joao_never_ask = order_never_asked(data, "joao")
        joao_never_went = days_off(data, "joao")

        text = [
            f"{maria_eats}\n"
            f"{arnaldo_ask_hamburguer}\n"
            f"{joao_never_ask}\n"
            f"{joao_never_went}\n"
        ]

        print(text)

        with open("data/mkt_campaign.txt", "w") as f:
            f.writelines(text)

    else:
        raise FileNotFoundError(
            f"No such file or directory: '{path_to_file}'"
        )
