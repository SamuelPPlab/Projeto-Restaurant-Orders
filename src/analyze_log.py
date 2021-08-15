from csv import DictReader


def prato_mais_pedido_por_maria(informacoes):
    info_pedidos = {}

    for pedido in informacoes:
        if pedido["nome"] == "maria":
            if pedido["pedido"] in info_pedidos:
                info_pedidos[pedido["pedido"]] += 1
            else:
                info_pedidos[pedido["pedido"]] = 1

    return max(info_pedidos, key=info_pedidos.get)


def quantas_vezes_arnaldo_pediu_hamburguer(informacoes):
    return [
        pedido["pedido"]
        for pedido in informacoes
        if pedido["nome"] == "arnaldo"
    ].count("hamburguer")


def quais_pratos_joao_nunca_pediu(informacoes):
    pedidosJoao = set()
    todosPedidos = set()

    for pedido in informacoes:
        todosPedidos.add(pedido["pedido"])
        if(pedido["nome"] == "joao"):
            pedidosJoao.add(pedido["pedido"])

    return todosPedidos.difference(pedidosJoao)


def quais_dias_joao_nunca_foi_na_lanchonete(informacoes):
    diasJoao = set()
    todosDias = set()

    for pedido in informacoes:
        todosDias.add(pedido["dia"])
        if(pedido["nome"] == "joao"):
            diasJoao.add(pedido["dia"])

    return todosDias.difference(diasJoao)


def analyze_log(path_to_file):
    with open(path_to_file, mode="r") as res:
        informacoes = list(
            DictReader(res, fieldnames=["nome", "pedido", "dia"])
        )

    with open("data/mkt_campaign.txt", "w") as txt:
        txt.write(
            f"{prato_mais_pedido_por_maria(informacoes)}\n"
            f"{quantas_vezes_arnaldo_pediu_hamburguer(informacoes)}\n"
            f"{quais_pratos_joao_nunca_pediu(informacoes)}\n"
            f"{quais_dias_joao_nunca_foi_na_lanchonete(informacoes)}\n"
        )
