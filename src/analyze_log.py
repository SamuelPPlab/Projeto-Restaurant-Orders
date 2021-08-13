import csv


def relatory(header, body):
    relatory = {}
    relatory[header[0]] = {"comida": [header[1]], "dia": [header[2]]}
    for lista in body:
        if lista[0] not in relatory:
            relatory[lista[0]] = {}
            relatory[lista[0]]["comida"] = []
            relatory[lista[0]]["comida"].append(lista[1])
            relatory[lista[0]]["dia"] = []
            relatory[lista[0]]["dia"].append(lista[2])
        else:
            relatory[lista[0]]["comida"].append(lista[1])
            relatory[lista[0]]["dia"].append(lista[2])

    return relatory


def comida_maria(comidas):
    contador = {}
    mais_frequente = comidas[0]

    for comida in comidas:
        if comida not in contador:
            contador[comida] = 1
        else:
            contador[comida] += 1

    if contador[comida] > contador[mais_frequente]:
        mais_frequente = comida

    return mais_frequente


def joao_nunca_comeu(pratos, comida):
    joao_nunca = set()
    for prato in pratos:
        if prato not in comida:
            joao_nunca.add(prato)

    return joao_nunca


def joao_nunca_foi(dias, dia):
    joao_nunquinha = set()
    for day in dias:
        if day not in dia:
            joao_nunquinha.add(day)

    return joao_nunquinha


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        leitor = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = leitor

    relatorio = relatory(header, data)
    maria_come_comida = comida_maria(relatorio["maria"]["comida"])
    arnaldo_hamburger = relatorio["arnaldo"]["comida"].count('hamburguer')

    pratos = ['coxinha', 'misto-quente', 'pizza', 'hamburguer']
    joao_nunca_pediu = joao_nunca_comeu(pratos, relatorio["joao"]["comida"])

    dias = ['segunda-feira', 'sabado', 'terça-feira']
    joao_nunca_saiu = joao_nunca_foi(dias, relatorio["joao"]["dia"])

    with open("data/mkt_campaign.txt", "w") as file:
        file.writelines([
            f"{maria_come_comida}\n",
            f"{arnaldo_hamburger}\n",
            f"{joao_nunca_pediu}\n",
            f"{joao_nunca_saiu}\n",
        ])
    # referência: Luíse Rios

#     print(maria_comida)
#     print(arnaldo_hamburger)
#     print(joao_nunca)
#     print(joao_nunca_saiu)


# analyze_log("data/orders_1.csv")
