from csv import DictReader


def analyze_log(path_to_file):
    with open(path_to_file, mode="r") as res:
        pedidos = list(DictReader(res, fieldnames=["nome", "pedido", "dia"]))

    # Arnaldo
    hamburguersForArnaldo = [
        pedido["pedido"] for pedido in pedidos if pedido["nome"] == "arnaldo"
    ].count("hamburguer")

    # Maria
    todosPedidosDaMaria = {}

    for pedido in pedidos:
        if (
            pedido["nome"] == "maria"
            and pedido["pedido"] in todosPedidosDaMaria
        ):
            todosPedidosDaMaria[pedido["pedido"]] += 1
        else:
            todosPedidosDaMaria[pedido["pedido"]] = 1

    pratoMaisPedidoDaMaria = max(
        todosPedidosDaMaria, key=todosPedidosDaMaria.get
    )

    pratosDoJoão = set()
    todosOsPratos = set()
    diasQueJoaoFrequenta = set()
    todosDias = set()

    for pedido in pedidos:
        todosOsPratos.add(pedido["pedido"])

    for pedido in pedidos:
        if pedido["nome"] == "joao":
            pratosDoJoão.add(pedido["pedido"])

    pratoNuncaPedidoPorJoao = todosOsPratos.difference(pratosDoJoão)

    for pedido in pedidos:
        todosDias.add(pedido["dia"])

    for pedido in pedidos:
        if pedido["nome"] == "joao":
            diasQueJoaoFrequenta.add(pedido["dia"])

    diasQueJoaoNaoFrequenta = todosDias.difference(diasQueJoaoFrequenta)

    with open("data/mkt_campaign.txt", "w") as txt:
        txt.write(
            f"{pratoMaisPedidoDaMaria}\n"
            f"{hamburguersForArnaldo}\n"
            f"{pratoNuncaPedidoPorJoao}\n"
            f"{diasQueJoaoNaoFrequenta}\n"
        )
