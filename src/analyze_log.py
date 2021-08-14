import csv
import os
import sys


def most_requests_maria(orders):
    orders = {
        order["pedido"]: orders.count(order)
        for order in orders
        if order["cliente"] == "maria"
    }
    return max(orders, key=orders.get)


def path_and_format(file_name, file_ext):
    if not os.path.exists(file_name):
        print(f"Arquivo {file_name} não econtrado")
        return True
    if not file_name.endswith(file_ext):
        print("Formato inválido")
        return True
    return False


def most_food_arnaldo(orders):
    return [
        orders.count(order)
        for order in orders
        if order["pedido"] == "misto-quente" and order["cliente"] == "arnaldo"
    ][0]


def never_requested_joao(orders):
    products = set([order["pedido"] for order in orders])
    joao_orders_products = set(
        [order["pedido"] for order in orders if order["cliente"] == "joao"]
    )
    return products.difference(joao_orders_products)


def never_visited_joao(orders):
    days = set([order["dia"] for order in orders])
    joao_orders = set(
        [order["dia"] for order in orders if order["cliente"] == "joao"]
    )
    return days.difference(joao_orders)


def import_csv(file):
    if path_and_format(file, ".csv"):
        return True
    objetct_data = ""
    objetct_res = {}
    with open(file) as file:
        objetct_data = csv.reader(file, delimiter=",")
        for values in objetct_data:
            if values[0] not in objetct_res:
                objetct_res[values[0]] = {
                    "Foods": [],
                    "Days": [],
                }
            objetct_res[values[0]]["Foods"].append(values[1])
            objetct_res[values[0]]["Days"].append(values[2])
    return objetct_res


def analyse_log(file):
    orders_list = []
    try:
        with open(file, newline="") as file:
            fields_title = ["cliente", "pedido", "dia"]
            reader = csv.DictReader(file, fieldnames=fields_title)
            for row in reader:
                orders_list.append(row)
    except FileNotFoundError:
        print(f"Arquivo {file} não encontrado", file=sys.stderr)
    else:
        order_by_maria = most_requests_maria(orders_list)
        frequency_by_arnaldo = str(most_food_arnaldo(orders_list))
        never_ordered_by_joao = never_requested_joao(orders_list)
        visited_by_joao = never_visited_joao(orders_list)
        with open("mkt_campaign.txt", "w") as file:
            lines = [
                f"{order_by_maria}\n",
                f"{frequency_by_arnaldo}\n",
                f"{never_ordered_by_joao}\n",
                f"{visited_by_joao}\n",
            ]
            file.writelines(lines)
