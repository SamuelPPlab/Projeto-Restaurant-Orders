import csv


def csv_reader(file):
    ordersData = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            ordersData.append(row)
    return ordersData


def items(client, orders):
    clientOrders = []
    for order in orders:
        if (order[0] == client):
            clientOrders.append(order[1])
    return clientOrders


def days(client, orders):
    clientOrders = []
    for order in orders:
        if (order[0] == client):
            clientOrders.append(order[2])
    return clientOrders


def count_item(item, clientOrders):
    return(clientOrders.count(item))


def item_most_ordered_by_client(clientOrders):
    return max(clientOrders, key=clientOrders.count)


def get_menu(orders):
    return set(map(lambda x: x[1], orders))


def get_days(orders):
    return set(map(lambda x: x[2], orders))


def item_never_ordered(clientOrders, menu):
    return menu.symmetric_difference(clientOrders)


def day_never_visited(clientOrders, days):
    return(days.symmetric_difference(clientOrders))


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(
            f"No such file or directory: '{path_to_file}'"
        )
    orders = csv_reader(path_to_file)
    maria_most = item_most_ordered_by_client(items('maria', orders))
    arnaldo_orders = count_item('hamburguer', items('arnaldo', orders))
    never_joao = item_never_ordered(items('joao', orders), get_menu(orders))
    never_day_joao = day_never_visited(days('joao', orders), get_days(orders))
    rows = [
        f'{maria_most}\n',
        f'{arnaldo_orders}\n',
        f'{never_joao}\n',
        f'{never_day_joao}',
    ]
    with open('data/mkt_campaign.txt', 'w') as txt_file:
        txt_file.writelines(rows)
