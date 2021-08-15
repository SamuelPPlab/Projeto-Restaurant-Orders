import csv


def analyze_log(path_to_file):
    """
        - Abre arquivo csv,
        - Itera sobre resultados transformando itens em dict
        - Busca
            - Prato mais pedido por 'maria';
            - Quantas vezes 'arnaldo' pediu 'hamburguer';
            - Os pratos que 'joao' nunca pediu;
            - Dias em que 'joao' nunca foi na lanchonete
        - Salva o resultado em um arquivo txt
    """

    orders = read_file(path_to_file)

    maria_often_orders = most_common_order_by_client(orders, "maria")

    arnaldo_ordered_buger = arnaldo_ordered_hamburger(orders)

    joao_never_ordered = client_never_ordered(orders, "joao")

    joao_didnt_go = client_didnt_show_up(orders, "joao")

    answers = [
        maria_often_orders,
        arnaldo_ordered_buger,
        joao_never_ordered,
        joao_didnt_go
    ]

    write_in_file("data/mkt_campaign.txt", answers)


def read_file(path):
    # Ref: Luíse Rios
    with open(path, 'r') as restaurant_data:
        data = csv.reader(restaurant_data, delimiter=',', quotechar='"')
        orders_data = dict()
        for item in data:
            orders_data["name"] = item[0]
            orders_data["order"] = item[1]
            orders_data["day_in_week"] = item[2]
        return list(orders_data)


def write_in_file(path, answers):
    # Ref: Samanta Below
    with open(path, 'w') as restaurant_data:
        _lines = [f"{answer}\n" for answer in answers]
        restaurant_data.writelines(_lines)


def orders_by_client(orders, client):
    return [order["order"] for order in orders if order["name"] == client]


def order_options(orders):
    return set([order["order"] for order in orders])


def order_counter(orders, client):
    all_orders = dict()
    for order in orders_by_client(orders, client):
        if order in all_orders:
            all_orders[order] += 1
        else:
            all_orders[order] = 1
    return all_orders


def most_common_order_by_client(orders, client):
    # Ref: https://bit.ly/3xMOHiF
    all_orders = order_counter(orders, client)
    inverse = [(value, key) for key, value in all_orders.items()]
    return max(inverse)[1]


def arnaldo_ordered_hamburger(orders):
    ordered_hamburger_counter = 0
    for order in orders:
        if order["order"] == "hamburguer" and order["name"] == "arnaldo":
            ordered_hamburger_counter += 1
    return ordered_hamburger_counter


def client_never_ordered(orders, client):
    all_orders = set(order_options(orders))
    joao_ordered = set(orders_by_client(orders, client))
    return all_orders.difference(joao_ordered)


def work_days(orders):
    restaurant_work_days = set()
    for day in orders:
        restaurant_work_days.add(day["day_in_week"])
    return restaurant_work_days


def client_didnt_show_up(orders, client):
    restaurant_work_days = work_days(orders)
    client_showed_up = set(
        day["day_in_week"] for day in orders if day["name"] == client
    )
    return restaurant_work_days.difference(client_showed_up)
