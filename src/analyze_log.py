import csv
import collections


def analyze_log(path_to_file):
    lista = []
    with open(path_to_file, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",")
        for row in spamreader:
            if row[0] == "maria":
                lista.append(row[1])
    # result2 = collections.Counter(lista).most_common()
    result1 = collections.Counter(lista).most_common(1)[0][0]
    print(result1)
    # print("teste", result2)

    with open("data/mkt_campaign.txt", "w") as f:
        f.write(result1)


analyze_log("data/orders_1.csv")
