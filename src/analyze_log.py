import csv
from collections import Counter


def most_orders(name, data):
    client = []
    for item in data:
        if item[0] == name:
            client.append(item[1])
    result = Counter(client).most_common(1)[0][0]
    return result


def order_count(name, meal, data):
    count = 0
    for item in data:
        if item[0] == name and item[1] == meal:
            count += 1
    return count


def not_ordered(name, data):
    meals = set()
    items = set()
    for item in data:
        meals.add(item[1])
    for item in data:
        if item[0] == name:
            items.add(item[1])
    return meals.difference(items)


def not_orders(name, data):
    days = set()
    client_days = set()
    for item in data:
        days.add(item[2])
    for client in data:
        if client[0] == name:
            client_days.add(client[2])
    return days.difference(client_days)


def csv_reader(path_to_file):
    with open(path_to_file) as file:
        return list(csv.reader(file))


def analyze_log(path_to_file):
    result = ""
    data = csv_reader(path_to_file)
    maria_most_orders = most_orders("maria", data)
    arnaldo_count = order_count("arnaldo", "hamburguer", data)
    joao_no_order = not_ordered("joao", data)
    joao_days = not_orders("joao", data)
    result = (
        f"{maria_most_orders}\n{arnaldo_count}\n{joao_no_order}\n{joao_days}"
    )
    f = open("data/mkt_campaign.txt", "w")
    f.write(result)
    f.close()
