import csv


def open_file(path):
    result = []
    with open(path) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in reader:
            result.append(tuple(row))

    return result


def write_file(LINES):
    with open('data/mkt_campaign.txt', mode='w') as file:
        file.writelines(LINES)


def consult_most_frequent_order_by_client(file, client):
    result = dict((x, file.count(x)) for x in set(file) if client in x)
    dish = ''
    most_frequent = 0
    for k, v in result.items():
        if v > most_frequent:
            most_frequent = v
            dish = k
    return dish[1]


def order_quantity_by_client(file, client, dish):
    file_client = dict((x, file.count(x)) for x in set(file) if client in x)
    for key, value in file_client.items():
        if dish in key:
            return value


def never_order_by_client(file, client):
    dishes = set()
    dishes_client = set()

    for value in file:
        dishes.add(value[1])
        if value[0] == client:
            dishes_client.add(value[1])
    return dishes.difference(dishes_client)


def days_never_attended_by_client(file, client):
    days = set()
    days_client = set()

    for value in file:
        days.add(value[2])
        if value[0] == client:
            days_client.add(value[2])

    return days.difference(days_client)


def analyze_log(path_to_file):
    data = open_file(path_to_file)
    maria = consult_most_frequent_order_by_client(
        data, 'maria')
    arnaldo = order_quantity_by_client(
        data,  'arnaldo', 'hamburguer')
    joao_never_order = never_order_by_client(data, 'joao')
    joao_never_atended = days_never_attended_by_client(data, 'joao')

    write_file(
        f'{maria}\n{arnaldo}\n{joao_never_order}\n{joao_never_atended}')


# analyze_log('data/orders_1.csv')
