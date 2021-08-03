from csv import DictReader


def analyze_log(path_to_file):
    with open(path_to_file, mode='r') as content:
        orders = list(DictReader(
            content, fieldnames=['name', 'product', 'day']
        ))

    maria_orders = {}
    arnaldo_hamburguer_count = [
        order['product']
        for order in orders if order['name'] == 'arnaldo'
    ].count('hamburguer')

    joao_ask = set()
    joao_went = set()

    dishes = set([order['product'] for order in orders])
    days = set([order['day'] for order in orders])

    for order in orders:
        if order['name'] == 'joao':
            joao_ask.add(order['product'])
            joao_went.add(order['day'])

        if order['name'] == 'maria':
            if order['product'] in maria_orders:
                maria_orders[order['product']] += 1
            else:
                maria_orders[order['product']] = 1

    maria_more_request = max(maria_orders, key=maria_orders.get)

    with open('data/mkt_campaign.txt', 'w') as txt:
        txt.write(
            f'{maria_more_request}\n'
            f'{arnaldo_hamburguer_count}\n'
            f'{dishes.difference(joao_ask)}\n'
            f'{days.difference(joao_went)}'
        )
