import csv


def readCsv(path):
    log = []
    with open(path, 'r',) as file:
        reader = csv.reader(file, delimiter='\n')
        for line in reader:
            log.append(line)
    return log


def writeTxt(path, conteudo):
    with open(path, 'w',) as file:
        for line in conteudo:
            file.writelines(line)


def produtos(log):
    all_products = set()
    for pedido in log:
        cliente = pedido[0].split(',')
        all_products.add(cliente[1])
    return all_products


def diasSemana(log):
    semana = set()
    for pedido in log:
        cliente = pedido[0].split(',')
        semana.add(cliente[2])
    return semana


def findClient(log, nomeCliente):
    for pedido in log:
        cliente = pedido[0].split(',')
        if(cliente[0] == nomeCliente):
            return cliente[1]


def findFood(log, nomeCliente, food):
    count = 0
    for pedido in log:
        cliente = pedido[0].split(',')
        if(cliente[0] == nomeCliente):
            if(cliente[1] == food):
                count += 1
    return count


def foodNuncaPedido(log, nomeCliente, produtos):
    produto = set(produtos)
    for pedido in log:
        cliente = pedido[0].split(',')
        if(cliente[0] == nomeCliente):
            produto.discard(cliente[1])
    return produto


def diasNuncaLanchonete(log, nomeCliente, dias_semana):
    produto = set(dias_semana)
    for pedido in log:
        cliente = pedido[0].split(',')
        if(cliente[0] == nomeCliente):
            produto.discard(cliente[2])
    return produto


def analyze_log(path_to_file):
    log = readCsv(path_to_file)
    all_produtos = produtos(log)
    dias_semana = diasSemana(log)
    writeTxt('data/mkt_campaign.txt',
             [
                 f"{findClient(log, 'maria')}\n",
                 f"{findFood(log, 'arnaldo', 'hamburguer')}\n",
                 f"{foodNuncaPedido(log, 'joao', all_produtos)}\n",
                 f"{diasNuncaLanchonete(log, 'joao', dias_semana)}\n",
             ])
