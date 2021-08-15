import csv


def check_and_make_orders(client, order, day, orders):
    if (client not in orders.keys()):
        orders[client] = {"day": set(), "all_orders": dict()}

    if order not in orders[client]["all_orders"].keys():
        orders[client]["all_orders"][order] = 1
    else:
        orders[client]["all_orders"][order] += 1
    orders[client]["day"].add(day)


def write_txt_file(object, orders, dishes, joao_dishes, all_days):
    with open("data/mkt_campaign.txt", "w") as txt_file:
        txt_file.write(f"{max(object, key=object.get)}\n")
        txt_file.write(f"{orders['arnaldo']['all_orders']['hamburguer']}\n")
        txt_file.write(f"{dishes - joao_dishes}\n")
        txt_file.write(f"{all_days - orders['joao']['day']}\n")


def analyze_log(path_to_file):
    orders = dict()
    dishes = set()
    all_days = set()
    with open(path_to_file, newline="") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            client, order, day = row
            dishes.add(order)
            all_days.add(day)
            check_and_make_orders(client, order, day, orders)

    maria_object = orders["maria"]["all_orders"]
    joao_dishes = set(orders['joao']['all_orders'].keys())
    write_txt_file(maria_object, orders, dishes, joao_dishes, all_days)
