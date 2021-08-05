import csv


def open_file(file_open):
    with open(file_open) as file:
        file_reader = csv.reader(file)
        file = list(file_reader)
    return file


def analyze_log(path_to_file):
    report = ""
    more_request_maria = ""
    orders_maria = []
    orders_arnaldo = []
    orders_joao = set()
    order_count = 0
    qty_hambuguer_arnaldo = 0
    all_dishes = set()
    joao_days = set()
    days = set()
    orders = open_file(path_to_file)
    report_all = {}
    for name, order, day in orders:
        count = orders_maria.count(order)
        all_dishes.add(order)
        days.add(day)
        if name == "joao":
            orders_joao.add(order)
            joao_days.add(day)
        if name == "arnaldo":
            orders_arnaldo.append(order)
        if name == "maria":
            orders_maria.append(order)
        if count > order_count:
            order_count = count
            more_request_maria = order

    days_joao_never_was = days.difference(joao_days)
    dishes_never_ordered_joao = all_dishes.difference(orders_joao)
    qty_hambuguer_arnaldo = orders_arnaldo.count("hamburguer")
    report = (
        f"{more_request_maria}\n"
        f"{qty_hambuguer_arnaldo}\n"
        f"{dishes_never_ordered_joao}\n"
        f"{days_joao_never_was}"
    )

    return report


print(analyze_log("data/orders_1.csv"))
