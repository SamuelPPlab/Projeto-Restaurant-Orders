import csv
import collections


def analyze_log(path_to_file):
    with open(path_to_file, newline="") as csvfile:
        importer = csv.reader(csvfile, delimiter=",")
        maria = []
        arnaldo_hamburguer = 0
        todos = set()
        joao = set()
        todos_os_dias = set()
        joao_foi = set()
        for row in importer:
            # print(row)
            if row[0] == "maria":
                maria.append(row[1])
            if row[0] == "arnaldo" and row[1] == "hamburguer":
                arnaldo_hamburguer += 1
            todos.add(row[1])
            if row[0] == "joao":
                joao.add(row[1])
                joao_foi.add(row[2])
            todos_os_dias.add(row[2])

    mais_pedido_pela_maria = collections.Counter(maria).most_common(1)[0][0]

    conteudo = f"{mais_pedido_pela_maria}\n"
    conteudo += f"{arnaldo_hamburguer}\n"
    conteudo += f"{todos.difference(joao)}\n"
    conteudo += f"{todos_os_dias.difference(joao_foi)}"

    # print("conteudo", conteudo)
    with open('data/mkt_campaign.txt', 'w') as f:
        f.write(conteudo)

    # print("Pratos pedidos pela Maria: ", maria)
    # print("O mais pedido pela Maria: ", mais_pedido_pela_maria)
    # print("Todos os alimentos: ", todos)
    # print("O que João nunca pediu", todos.difference(joao))
    # print("Todos os dias: ", todos_os_dias)
    # print("Dias que João não foi: ", todos_os_dias.difference(joao_foi))


