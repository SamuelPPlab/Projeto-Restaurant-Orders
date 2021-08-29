import csv
import collections


def analyze_log(path_to_file):
    count = 0
    results = []
    products = set()
    day = set()
    week = set()
    demand = set()

    with open(path_to_file, newline="") as file:

        requests = csv.reader(file, delimiter=",")

        for consumer in requests:
            products.add(consumer[1])
            week.add(consumer[2])

            if consumer[0] == "arnaldo" and consumer[1] == "hamburguer":
                count += 1

            if consumer[0] == "maria":
                results.append(consumer[1])

            if consumer[0] == "joao":
                day.add(consumer[2])
                demand.add(consumer[1])

    consumed = f"{collections.Counter(results).most_common(1)[0][0]}\n"
    consumed += f"{count}\n"
    consumed += f"{products.difference(demand)}\n"
    consumed += f"{week.difference(day)}\n"

    with open("data/mkt_campaign.txt", "w") as write_file:
        write_file.write(consumed)


analyze_log("data/orders_1.csv")
