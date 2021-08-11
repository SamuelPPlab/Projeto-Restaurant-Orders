import csv
import collections


def analyze_log(path_to_file):
    list = []
    count = 0
    list_product = set()
    day = set()
    demand = set()
    week = set()

    with open(path_to_file, newline="") as file:
        requests = csv.reader(file, delimiter=",")
        for consumer in requests:
            list_product.add(consumer[1])
            week.add(consumer[2])
            if consumer[0] == "maria":
                list.append(consumer[1])
            if consumer[0] == "arnaldo" and consumer[1] == "hamburguer":
                count += 1
            if consumer[0] == "joao":
                day.add(consumer[2])
                demand.add(consumer[1])

    most_consumed = f"{collections.Counter(list).most_common(1)[0][0]}\n"
    most_consumed += f"{count}\n"
    most_consumed += f"{list_product.difference(demand)}\n"
    most_consumed += f"{week.difference(day)}\n"

    with open("data/mkt_campaign.txt", "w") as write_file:
        write_file.write(most_consumed)


analyze_log("data/orders_1.csv")
