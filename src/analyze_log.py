import csv


def leitor_arquivo(caminho):
    with open(caminho) as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=",")
        pedidos = list(leitor_csv)
    return pedidos


def mais_pedido(nome, pedidos):
    mais_pedido = ""
    for pedido in pedidos:
        if pedido[0] == nome:
            mais_pedido = pedido[1]
            break
    return mais_pedido


def qunatidade(nome, prato, pedidos):
    quantidades = set()
    for pedido in pedidos:
        if pedido[0] == nome and pedido[1] == prato:
            quantidades.add(pedido[1])
    return len(quantidades)


def nunca_pedidos(nome, pedidos):
    pedidos_pessoa = set()
    todos_pedidos = set()
    for pedido in pedidos:
        todos_pedidos.add(pedido[1])
    for cliente in pedidos:
        if cliente[0] == nome:
            pedidos_pessoa.add(cliente[1])
    return todos_pedidos.difference(pedidos_pessoa)


def dias_sem_pedir(nome, pedidos):
    dias_com_pedidos = set()
    dias = set()
    for pedido in pedidos:
        dias.add(pedido[2])
    for pedido in pedidos:
        if pedido[0] == nome:
            dias_com_pedidos.add(dia[2])
    return dias.difference(dias_com_pedidos)


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    orders = leitor_arquivo(path_to_file)
    with open("data/mkt_campaign.txt", "w") as analyze_file:
        analyze_file.write(f"{mais_pedido("maria", orders)}\n")
        analyze_file.write(
            f"{qunatidade("arnaldo","hamburguer", orders)}\n"
        )
        analyze_file.write(
            f"{nunca_pedidos("joao", orders)}\n"
        )
        analyze_file.write(f"{dias_sem_pedir("joao", orders)}\n")
    
