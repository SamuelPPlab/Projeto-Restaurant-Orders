import csv


def open_file(file_open):
    with open(file_open) as file:
        file_reader = csv.reader(file)
        file = list(file_reader)
    return file


def writer_file(file_write, content):
    with open(file_write, "w") as file:
        file.write(content)


def configuring_report(name, info_by_person):
    if name not in info_by_person:
        info_by_person[name] = {}
        info_by_person[name]["days"] = set()
        info_by_person[name]["orders"] = set()
        info_by_person[name]["all_orders"] = []
        info_by_person[name]["most_ordered_quantity"] = {}
        info_by_person[name]["most_requested_item"] = ""


def most_requested(name, list):
    return list[name]["most_requested_item"]


def qty_order(name, order, list):
    return list[name]["most_ordered_quantity"][order]


def orders_never_made(name, all_dishes, list):
    return all_dishes.difference(list[name]["orders"])


def not_days(name, days, list):
    return days.difference(list[name]["days"])


def analyze_log(path_to_file):
    report = ""
    all_dishes = set()
    days = set()
    orders = open_file(path_to_file)
    info_by_person = {}
    for name, order, day in orders:
        all_dishes.add(order)
        days.add(day)
        configuring_report(name, info_by_person)

        if order not in info_by_person[name]["most_ordered_quantity"]:
            info_by_person[name]["most_ordered_quantity"][order] = 0

        info_by_person[name]["days"].add(day)
        info_by_person[name]["orders"].add(order)
        info_by_person[name]["all_orders"].append(order)
        info_by_person[name]["most_ordered_quantity"][order] += 1
        count = 0
        for item, qtd in info_by_person[name]["most_ordered_quantity"].items():

            if qtd > count:
                count = qtd
                info_by_person[name]["most_requested_item"] = item

    most_requested_maria = most_requested("maria", info_by_person)
    qtd_hambuguer_arnaldo = qty_order("arnaldo", "hamburguer", info_by_person)
    orders_never_made_joao = orders_never_made(
        "joao", all_dishes, info_by_person
    )
    not_days_joao = not_days("joao", days, info_by_person)

    report = (
        f"{most_requested_maria}\n"
        f"{qtd_hambuguer_arnaldo}\n"
        f"{orders_never_made_joao}\n"
        f"{not_days_joao}\n"
    )

    writer_file("data/mkt_campaign.txt", report)
