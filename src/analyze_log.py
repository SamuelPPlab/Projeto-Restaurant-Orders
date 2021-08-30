from collections import Counter
import csv


def most_ordered(history, client):
    orders = list(
        order["item"] for order in history
        if order["client"] == client
    )
    result = dict(Counter(orders))
    # tip from @vanessaberbidi
    return max(result, key=lambda k: result[k])


def order_counter(history, client, item):
    orders = list(
        order["item"] for order in history
        if order["client"] == client and order["item"] == item
    )
    result = dict(Counter(orders))
    return result.get(item)


def never_ordered(history, client):
    all_items = set(order["item"] for order in history)
    items_ordered = set(
        order["item"] for order in history
        if order["client"] == client
    )
    return all_items.difference(items_ordered)


def days_never_visited(history, client):
    all_days = set(order["week_day"] for order in history)
    days_visited = set(
        order["week_day"] for order in history
        if order["client"] == client
    )
    return all_days.difference(days_visited)


def analyze_log(path_to_file):
    with open(path_to_file) as source:
        keys = ["client", "item", "week_day"]
        reader = csv.DictReader(source, fieldnames=keys)
        data = list(row for row in reader)

        content = [
            f"{most_ordered(data, 'maria')}\n",
            f"{order_counter(data, 'arnaldo', 'hamburguer')}\n",
            f"{never_ordered(data, 'joao')}\n",
            f"{days_never_visited(data, 'joao')}\n"
        ]

    with open("./data/mkt_campaign.txt", 'w') as target:
        target.writelines(content)
