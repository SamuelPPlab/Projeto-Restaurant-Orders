from csv import DictReader

def resposta_maria(pedidos):
    todosPedidosDaMaria = {}

    for pedido in pedidos:
        if (
            pedido["nome"] == "maria"
            and pedido["pedido"] in todosPedidosDaMaria
        ):
            todosPedidosDaMaria[pedido["pedido"]] += 1
        else:
            todosPedidosDaMaria[pedido["pedido"]] = 1

    return max( todosPedidosDaMaria, key=todosPedidosDaMaria.get )


def resposta_Arnaldo(pedidos):
    return [
        pedido["pedido"] for pedido in pedidos if pedido["nome"] == "arnaldo"
    ].count("hamburguer")


def pratoNuncaPedidoPorJoao(pedidos):
    pratosDoJoão = set()
    todosOsPratos = set()

    for pedido in pedidos:
        todosOsPratos.add(pedido["pedido"])

    for pedido in pedidos:
        if pedido["nome"] == "joao":
            pratosDoJoão.add(pedido["pedido"])

    return todosOsPratos.difference(pratosDoJoão)


def diasQueJoaoNaoFrequenta(pedidos):
    diasQueJoaoFrequenta = set()
    todosDias = set()

    for pedido in pedidos:
        todosDias.add(pedido["dia"])

    for pedido in pedidos:
        if pedido["nome"] == "joao":
            diasQueJoaoFrequenta.add(pedido["dia"])

    return todosDias.difference(diasQueJoaoFrequenta)

def analyze_log(path_to_file):
    with open(path_to_file, mode="r") as res:
        pedidos = list(DictReader(res, fieldnames=["nome", "pedido", "dia"]))

    with open("data/mkt_campaign.txt", "w") as txt:
        txt.write(
            f"{resposta_maria(pedidos)}\n"
            f"{resposta_Arnaldo(pedidos)}\n"
            f"{pratoNuncaPedidoPorJoao(pedidos)}\n"
            f"{diasQueJoaoNaoFrequenta(pedidos)}\n"
        )
