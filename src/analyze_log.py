import csv
import collections


def analyze_log(path_to_file):
    maria = []
    hamburgers_arnaldo = 0
    pratos_joao_pediu = set()
    dias_joao_foi = set()
    pratos = set()
    dias_com_clientes = set()

    with open(path_to_file) as file:
        data = csv.reader(file, delimiter=",")
        for item in data:
            if item[0] == "maria":
                maria.append(item[1])
            if item[0] == "arnaldo" and item[1] == "hamburger":
                hamburgers_arnaldo = hamburgers_arnaldo + 1
            if item[0] == "joao":
                pratos_joao_pediu.add(item[1])
                dias_joao_foi.add(item[2])
            pratos.add(item[1])
            dias_com_clientes.add(item[2])

# https://docs.python.org/pt-br/3/library/collections.html
    prato_favorito_maria = collections.Counter(maria).most_common(1)[0][0]
    pratos_joao_nao_pediu = pratos.difference(pratos_joao_pediu)
    dias_joao_nunca_foi = dias_com_clientes.difference(dias_joao_foi)

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{prato_favorito_maria}\n"
            f"{hamburgers_arnaldo}\n"
            f"{pratos_joao_nao_pediu}\n"
            f"{dias_joao_nunca_foi}"
        )
        print(hamburgers_arnaldo)
