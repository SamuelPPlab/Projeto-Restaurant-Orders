import csv
from collections import Counter


def read_file(filename):
    try:
        with open(filename) as csvfile:
            fields = ['client', 'product', 'day']
            reader = csv.DictReader(csvfile, fieldnames=fields)
            results = list(row for row in reader)
            return results
    except ValueError:
        raise FileNotFoundError(f"No such file or directory: '{filename}'")


def most_ordered(results, client):
    products_by_client = list((
        item["product"] for item in results
        if item["client"] == client
    ))
    most_ordered_product = Counter(products_by_client).most_common()[0][0]
    return most_ordered_product


def count_order_by_client(results, client, product):
    products_by_client = list((
        item["product"] for item in results
        if item["client"] == client and item["product"] == product
    ))
    count_product = products_by_client.count(product)
    return count_product


def unordered_products_by_client(results, client):
    products = set((item["product"] for item in results))
    products_by_client = set((
        item["product"] for item in results
        if item["client"] == client
    ))
    unordered_products = products.difference(products_by_client)
    return unordered_products


def not_visited_days_by_client(results, client):
    days = set((item["day"] for item in results))
    visited_days_by_client = set((
        item["day"] for item in results
        if item["client"] == client
    ))
    days_not_visited = days.difference(visited_days_by_client)
    return days_not_visited


def write_file(new_file, format):
    with open(new_file, 'w') as file:
        file.writelines(format)


def analyze_log(path_to_file):
    file = read_file(path_to_file)

    format = [
        f"{most_ordered(file, 'maria')}\n",
        f"{count_order_by_client(file, 'arnaldo', 'hamburguer')}\n",
        f"{unordered_products_by_client(file, 'joao')}\n",
        f"{not_visited_days_by_client(file, 'joao')}\n"
    ]

    write_file("data/mkt_campaign.txt", format)
