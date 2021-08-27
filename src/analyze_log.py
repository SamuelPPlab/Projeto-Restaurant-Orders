from collections import Counter
import csv


def days_not_visit(results, client):
    days = set(item["day"] for item in results)
    visited_days_by_client = set(
        item["day"] for item in results
        if item["client"] == client
    )
    days_not_visit = days.difference(visited_days_by_client)
    return days_not_visit


def unorded_products(results, client):
    products = set(order["product"] for order in results)
    products_client = set(
        order["product"] for order in results
        if order["client"] == client
    )
    unorded_products = products.difference(products_client)
    return unorded_products


def count_order_by_client(results, client, product):
    products_client = list(
        order["product"] for order in results
        if order["client"] == client and order["product"] == product
    )
    count_product = products_client.count(product)
    return count_product


def most_orded(results, client):
    by_client = list(
        order["product"] for order in results
        if order["client"] == client
    )
    product = Counter(by_client).most_common()[0][0]
    return product


def analyze_log(path_to_file):

    with open(path_to_file) as csvfile:
        fields = ['client', 'product', 'day']
        reader = csv.DictReader(csvfile, fieldnames=fields)
        file = list(row for row in reader)

    format = [
        f"{most_orded(file, 'maria')}\n",
        f"{count_order_by_client(file, 'arnaldo', 'hamburguer')}\n",
        f"{unorded_products(file, 'joao')}\n",
        f"{days_not_visit(file, 'joao')}\n"
    ]

    with open("./data/mkt_campaign.txt", 'w') as file:
        file.writelines(format)
