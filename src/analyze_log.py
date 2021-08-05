import csv


def prato_favorito(nome, pedidos):
    prato_favorito = ""
    for pedido in pedidos:
        if pedido[0] == nome:
            prato_favorito = pedido[1]
            break
    return prato_favorito


def pratos_repetidos(nome, prato, pedidos):
    client_order = set()
    for pedido in pedidos:
        if pedido[0] == nome and pedido[1] == prato:
            client_order.add(pedido[1])
    return len(client_order)


def pratos_nunca_pedidos(nome, pedidos):
    pedido_client = set()
    todos_pedidos = set()
    for pedido in pedidos:
        todos_pedidos.add(pedido[1])
    for client in pedidos:
        if client[0] == nome:
            pedido_client.add(client[1])
    return todos_pedidos.difference(pedido_client)


def dias_sem_pedidos(nome, dias):
    dias_sem_pedidos = set()
    todos_dias = set()
    for dia in dias:
        todos_dias.add(dia[2])
    for dia in dias:
        if dia[0] == nome:
            dias_sem_pedidos.add(dia[2])
    return todos_dias.difference(dias_sem_pedidos)


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")

    with open(path_to_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        orders = list(csv_reader)

    clients_foods = ["maria", "joao", "arnaldo", "hamburguer"]

    with open("data/mkt_campaign.txt", "w") as analyze_file:
        analyze_file.write(f"{prato_favorito(clients_foods[0], orders)}\n")
        analyze_file.write(
            f"{pratos_repetidos(clients_foods[2],clients_foods[3], orders)}\n"
        )
        analyze_file.write(
            f"{pratos_nunca_pedidos(clients_foods[1], orders)}\n"
        )
        analyze_file.write(f"{dias_sem_pedidos(clients_foods[1], orders)}\n")
