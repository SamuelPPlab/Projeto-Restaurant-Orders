import csv


class Clients_data:
    def __init__(self, client, data):
        self.client = client
        self.orders = [row['order'] for row in data if client in row['client']]
        self.week_days = [row['week_day'] for row in data if client in row['client']]


def read_file(path_to_file):
    # https://github.com/tryber/sd-07-restaurant-orders/pull/6/files
    with open(path_to_file) as csv_file:
        keys = ['client', 'order', 'week_day']
        file_already_read = csv.DictReader(csv_file, fieldnames=keys)
        
        data = [row for row in file_already_read]
        return data


def get_favorite(client, list):
    maria = Clients_data(client, list)

    aux_count = {}
    marias_favorite = maria.orders[0]

    for marias_order in maria.orders:
        if marias_order not in aux_count:
            aux_count[marias_order] = 1
        else:
            aux_count[marias_order] += 1

        if aux_count[marias_order] > aux_count[marias_favorite]:
            marias_favorite = marias_order
    
    return marias_favorite


def how_many_times(client, list, order):
    arnaldo = Clients_data(client, list)
    many = (arnaldo.orders).count(order)
    return many


def dont_like(client, list):
    joao = Clients_data(client, list)
    all_orders = [row['order'] for row in list]
    joao_dont_like = set(all_orders) - set(joao.orders)
    return joao_dont_like


def days_not_visity(client, list):
    joao = Clients_data(client, list)
    all_week_days = [row['week_day'] for row in list]
    joao_dont_visit = set(all_week_days) - set(joao.week_days)
    return joao_dont_visit


def save_info_in_txt_file(
    marias_favorite,
    arnaldos_burger,
    joao_dont_like,
    joao_dont_visit
):
    FILE_PATH = 'data/mkt_campaign.txt'
    FILE_CONTENTS = [
        f'{marias_favorite}\n'
        f'{arnaldos_burger}\n'
        f'{joao_dont_like}\n'
        f'{joao_dont_visit}\n'
    ]

    with open(FILE_PATH, 'w') as file:
        file.writelines(FILE_CONTENTS)


def analyze_log(path_to_file):
    data = read_file(path_to_file)
    marias_favorite = get_favorite('maria', data)
    arnaldos_burger = how_many_times('arnaldo', data, 'hamburguer')
    joao_dont_like = dont_like('joao', data)
    joao_dont_visit = days_not_visity('joao', data)

    save_info_in_txt_file(
        marias_favorite,
        arnaldos_burger,
        joao_dont_like,
        joao_dont_visit
    )
