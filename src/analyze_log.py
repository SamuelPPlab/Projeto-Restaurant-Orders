import csv
import collections


def analyze_log(path_to_file):
    lista = []
    lista2 = 0
    pratosN = set()
    pedidosN = set()
    totalDias = set()
    userDias = set()
    with open(path_to_file, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",")
        for row in spamreader:
            pedidosN.add(row[1])
            totalDias.add(row[2])
            if row[0] == "maria":
                lista.append(row[1])
            if row[0] == "arnaldo" and row[1] == "hamburguer":
                lista2 += 1
            if row[0] == "joao":
                pratosN.add(row[1])
                userDias.add(row[2])
    # result2 = collections.Counter(lista).most_common()
    result1 = f"{collections.Counter(lista).most_common(1)[0][0]}\n"
    result1 += f"{lista2}\n"
    result1 += f"{pedidosN.difference(pratosN)}\n"
    result1 += f"{totalDias.difference(userDias)}\n"
    print(result1)
    # print("teste", result2)

    with open("data/mkt_campaign.txt", "w") as f:
        f.write(result1)


analyze_log("data/orders_1.csv")
