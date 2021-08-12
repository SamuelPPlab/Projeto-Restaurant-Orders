import csv
from collections import Counter


def read_file(path):
    with open(path) as csvfile:
        keys = ["name", "order", "week_day"]
        reader = csv.DictReader(csvfile, fieldnames=keys)
        data = []
        [data.append(row) for row in reader]
    return data


# Referencias: ajuda nos plantões de colegas e intrutores
def most_requested_dish(data, name):
    filter = []
    for item in data:
        if item["name"] == name:
            filter.append(item["order"])
    result = dict(Counter(filter))
    # https://stackoverflow.com/questions/13669252/what-is-key-lambda
    # https://www.ti-enxame.com/pt/python/o-que-isso-significa-key-lambda-x-x-1/1071942639/
    return max(result, key=lambda k: result[k])


def quantity_ordered(data, name, order):
    filter = []
    for item in data:
        if item["name"] == name:
            filter.append(item["order"])
    result = dict(Counter(filter))
    return result.get(order)


def never_asked(data, name):
    orders = set()
    orders_placed = set()
    for item in data:
        orders.add(item["order"])
        if item["name"] == name:
            orders_placed.add(item["order"])
            # diferença entre orders e orders_placed = pedidos feitos
    return orders.difference(orders_placed)


def never_was(data, name):
    days = set()
    days_week = set()
    for item in data:
        days.add(item["week_day"])
        if item["name"] == name:
            days_week.add(item["week_day"])
    return days.difference(days_week)


def analyze_log(path_to_file):
    if path_to_file.endswith('csv'):
        data = read_file(path_to_file)
        maria_eat = most_requested_dish(data, "maria")
        arnaldo_ask_hamburguer = quantity_ordered(
            data, "arnaldo", "hamburguer"
        )
        joao_never_ask = never_asked(data, "joao")
        joao_never_went = never_was(data, "joao")

        text = [
            f"{maria_eat}\n"
            f"{arnaldo_ask_hamburguer}\n"
            f"{joao_never_ask}\n"
            f"{joao_never_went}\n"
        ]

        with open("data/mkt_campaign.txt", "w") as f:
            f.writelines(text)

    else:
        raise FileNotFoundError(
            f"No such file or directory: '{path_to_file}'"
        )
