from collections import Counter
import csv


# Qual o prato mais pedido por 'maria'?
def request_maria(file_dict):
    pedidos_maria = [
        pedido["pedido"]
        for pedido in file_dict
        if pedido["cliente"] == "maria"
    ]
    return Counter(pedidos_maria).most_common(1)[0][0]

# Quantas vezes 'arnaldo' pediu 'hamburguer'?


def request_arnaldo(file_dict):
    pedidos_arnaldo = [
        pedido["pedido"]
        for pedido in file_dict
        if pedido["cliente"] == "arnaldo"
        # referencia Melissa-gomes
    ].count("hamburguer")
    return pedidos_arnaldo


def analyze_log(path_to_file):
    file_dict = []
    # Abrir o arquivo
    with open(path_to_file) as f:
        # ler a tabela
        file_dict = [
            row for row in csv.DictReader(
                f, fieldnames=["cliente", "pedido", "dia"])
        ]
        request_maria(file_dict)
        request_arnaldo(file_dict)

    with open("data/mkt_campaign.txt", mode="w") as f:
        f.writelines(
            f"{request_maria(file_dict)}\n"
            f"{request_arnaldo(file_dict)}\n"
        )

# if __name__ == "__main__":
#     analyze_log('./data/orders_1.csv')
