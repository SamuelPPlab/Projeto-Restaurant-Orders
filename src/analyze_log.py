def analyze_log(path_to_file):
    pedidos = _ler_pedidos_do_arquivo(path_to_file)
    print(pedidos[:3])

    #Qual o prato mais pedido por 'maria'?
    prato_maria = _prato_mais_pedido(pedidos, 'maria')

    #Quantas vezes 'arnaldo' pediu 'hamburguer'?
    hamburguers_arnaldo = _contagem_prato(pedidos, 'arnaldo', 'hamburguer')

    #Quais pratos 'joao' nunca pediu?
    joao_nunca_pediu = _todos_os_pratos(pedidos) - _pratos_pedidos(pedidos, 'joao')

    #Quais dias 'joao' nunca foi na lanchonete?
    joao_nao_veio_nos_dias = _dias_que_a_lanchonete_abre(pedidos) - _dias_pedidos(pedidos, 'joao')

    _escrever_no_arquivo('data/mkt_campaign.txt', [prato_maria, hamburguers_arnaldo, joao_nunca_pediu, joao_nao_veio_nos_dias])

def _ler_pedidos_do_arquivo(path):
    with open(path) as fd:
        return [line.strip().split(',') for line in fd.readlines()]

def _pedidos_da_pessoa(pedidos, pessoa):
    return (pedido for pedido in pedidos if pedido[0] == pessoa)

def _contagem_pratos(pedidos, pessoa):
    contagem_pratos = dict()
    for pedido in _pedidos_da_pessoa(pedidos, pessoa):
        prato = pedido[1]
        if prato in contagem_pratos:
            contagem_pratos[prato] += 1
        else:
            contagem_pratos[prato] = 1
    return contagem_pratos

def _prato_mais_pedido(pedidos, pessoa):
    contagem_pratos = _contagem_pratos(pedidos, pessoa)
    return max(contagem_pratos, key=contagem_pratos.get)

def _contagem_prato(pedidos, pessoa, prato):
    contagem_pratos = _contagem_pratos(pedidos, pessoa)
    return contagem_pratos[prato]

def _todos_os_pratos(pedidos):
    return {pedido[1] for pedido in pedidos}

def _pratos_pedidos(pedidos, pessoa):
    return {pedido[1] for pedido in pedidos if pedido[0] == pessoa}

def _dias_que_a_lanchonete_abre(pedidos):
    return {pedido[2] for pedido in pedidos}

def _dias_pedidos(pedidos, pessoa):
    return {pedido[2] for pedido in pedidos if pedido[0] == pessoa}

def _escrever_no_arquivo(path, lines):
    with open(path, 'w') as fd:
        fd.writelines(f"{line}\n" for line in lines)


