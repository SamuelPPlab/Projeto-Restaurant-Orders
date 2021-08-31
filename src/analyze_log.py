import csv


def file_importer(path_to_file):
    log = []
    with open(path_to_file) as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            entry = {}
            entry['cliente'] = row[0]
            entry['pedido'] = row[1]
            entry['dia'] = row[2]
            log.append(entry)
    return log


def client_fetcher(log, cliente):
    pedidos_do_cliente = []
    for item in log:
        if (item['cliente'] == cliente):
            pedidos_do_cliente.append(item)
    return pedidos_do_cliente


def key_selector_counter(client_history, key):
    frequencia = {}
    for item in client_history:
        if item[key] not in frequencia:
            frequencia[item[key]] = 1
        else:
            frequencia[item[key]] += 1
    return frequencia


def key_selector_set(client_history, key):
    frequencia = {}
    for item in client_history:
        if item[key] not in frequencia:
            frequencia[item[key]] = True
    return frequencia.keys()


def pedido_mais_comum_de_maria(log):
    maria = client_fetcher(log, 'maria')
    counted_orders = list(key_selector_counter(maria, 'pedido').items())
    most_common_order = ''
    count_holder = 0
    for order in counted_orders:
        if order[1] > count_holder:
            count_holder = order[1]
            most_common_order = order[0]
    return most_common_order


def how_many_hamburguers(log):
    pedidos_do_arnaldo = client_fetcher(log, 'arnaldo')
    order_count = key_selector_counter(pedidos_do_arnaldo, 'pedido')
    return order_count['hamburguer']


def joao_never_ordered(log):
    pedidos_do_joao = client_fetcher(log, 'joao')
    pratos_disponiveis = set(key_selector_set(log, 'pedido'))
    ordered_by_joao = set(key_selector_set(pedidos_do_joao, 'pedido'))
    return pratos_disponiveis.difference(ordered_by_joao)


def joao_never_went(log):
    pedidos_do_joao = client_fetcher(log, 'joao')
    dias_da_semana_joao_foi = set(key_selector_set(pedidos_do_joao, 'dia'))
    dias_da_semana = set(key_selector_set(log, 'dia'))
    return dias_da_semana.difference(dias_da_semana_joao_foi)


def analyze_log(path_to_file):
    log = file_importer(path_to_file)
    arquivo = open('data/mkt_campaign.txt', 'w')
    all_strings = [
        f"{pedido_mais_comum_de_maria(log)}\n",
        f"{str(how_many_hamburguers(log))}\n",
        f"{str(joao_never_ordered(log))}\n",
        f"{str(joao_never_went(log))}\n"
    ]
    for string in all_strings:
        arquivo.write(string)

    arquivo.close()
