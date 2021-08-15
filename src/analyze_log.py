import csv


def most_orders_by_maria(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        products_maria = dict
        for row in csv_reader:
            client_maria = 'maria'
            if client_maria in row[0]:
                products_maria = row[1]
            return products_maria
        seen_before = set()
        repeated = set()
        for product in products_maria:
            if product in seen_before:
                repeated.add(product)
            else:
                seen_before.add(product)
            return repeated


def orders_by_arnaldo(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        products_arnaldo = dict
        count = 0
        for row in csv_reader:
            client_arnaldo = 'arnaldo'
            if client_arnaldo in row[0]:
                products_arnaldo = row[1]
                if products_arnaldo == 'hamburguer':
                    count += 1
                    return (str(count))


def orders_not_by_joao(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        products_joao = dict
        others_products = dict
        set_products_joao = set()
        set_others_products = set()
        for row in csv_reader:
            client_joao = 'joao'
            if client_joao in row[0]:
                products_joao = row[1]
                set_products_joao.add(products_joao)
            else:
                others_products = row[1]
                set_others_products.add(others_products)
        return(str(set_others_products.difference(set_products_joao)))


def days_not_by_joao(path_to_file):
    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        days_joao = dict
        others_days = dict
        set_days_joao = set()
        set_others_days = set()
        for row in csv_reader:
            client_joao = 'joao'
            if client_joao in row[0]:
                days_joao = row[2]
                set_days_joao.add(days_joao)
            else:
                others_days = row[2]
                set_others_days.add(others_days)
        return(str(set_others_days.difference(set_days_joao)))


def analyze_log(path_to_file):
    f = open("data/mkt_campaign.txt", "w")
    f.write(f'{most_orders_by_maria(path_to_file)}\n')
    f.write(f'{orders_by_arnaldo(path_to_file)}\n')
    f.write(f'{orders_not_by_joao(path_to_file)}\n')
    f.write(f'{days_not_by_joao(path_to_file)}\n')
    f.close()
