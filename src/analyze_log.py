import csv

def mais_pedido_por_maria(orders):
    count = {}
    pedidos_maria = [item[1] for item in orders if item[0] == 'maria']
    mais_frequente = pedidos_maria[0]

    for order in pedidos_maria:
        if order not in count:
            count[order] = pedidos_maria.count(order)
        if count[order] > count[mais_frequente]:
            mais_frequente = order

    return mais_frequente

def pedidos_hamburguer_por_arnaldo(orders):
    arnaldo_ambuguer_orders = [
        item[1] for item in orders
        if item[0] == 'arnaldo' and item[1] == 'hamburguer'
    ]
    return len(arnaldo_ambuguer_orders)

def nao_pedido_por_john(orders):
    pratos_do_john = [item[1] for item in orders if item[0] == 'joao']
    nao_sao_pratos_do_john = [
        item[1]
        for item in orders if pratos_do_john.count(item[1]) == 0
    ]

    return set(nao_sao_pratos_do_john)

def john_nao_estava_presente(orders):
    com_john = [
        item[2]
        for item in orders if item[0] == 'joao'
    ]
    sem_john = [
        item[2]
        for item in orders if com_john.count(item[2]) == 0
    ]

    return set(sem_john)


def analyze_log(path_to_file):
    with open(path_to_file, 'r') as logs:
        reader = csv.reader(logs, delimiter=',')
        orders = [item for item in reader]

    with open('data/mkt_campaign.txt', 'w') as arquivo:
        arquivo.write(f'{mais_pedido_por_maria(orders)}\n')
        arquivo.write(f'{pedidos_hamburguer_por_arnaldo(orders)}\n')
        arquivo.write(f'{nao_pedido_por_john(orders)}\n')
        arquivo.write(f'{john_nao_estava_presente(orders)}')
