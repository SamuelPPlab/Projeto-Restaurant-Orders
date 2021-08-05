import csv


def most_ordered_by_maria(orders):
    count = {}
    maria_orders = [item[1] for item in orders if item[0] == 'maria']
    most_frequent = maria_orders[0]

    for order in maria_orders:
        if order not in count:
            count[order] = maria_orders.count(order)
        if count[order] > count[most_frequent]:
            most_frequent = order

    return most_frequent


def count_arnaldo_buguer(orders):
    arnaldo_buguer_orders = [
        item[1] for item in orders
        if item[0] == 'arnaldo' and item[1] == 'hamburguer'
    ]
    return len(arnaldo_buguer_orders)


def not_ordered_by_john(orders):
    johns_plates = [item[1] for item in orders if item[0] == 'joao']
    not_johns_plates = [
        item[1]
        for item in orders if johns_plates.count(item[1]) == 0
    ]

    return set(not_johns_plates)


def john_not_present(orders):
    johns_days = [
        item[2]
        for item in orders if item[0] == 'joao'
    ]
    not_johns_days = [
        item[2]
        for item in orders if johns_days.count(item[2]) == 0
    ]

    return set(not_johns_days)


def analyze_log(path_to_file):
    with open(path_to_file, 'r') as logs:
        reader = csv.reader(logs, delimiter=',')
        orders = [item for item in reader]

    with open('data/mkt_campaign.txt', 'w') as arquivo:
        arquivo.write(f'{most_ordered_by_maria(orders)}\n')
        arquivo.write(f'{count_arnaldo_buguer(orders)}\n')
        arquivo.write(f'{not_ordered_by_john(orders)}\n')
        arquivo.write(f'{john_not_present(orders)}')
