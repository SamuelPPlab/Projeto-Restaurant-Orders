import csv
import collections


def analyze_log(path_to_file):
    list = []
    total_hamburgers = 0
    total_dishes = set()
    dishes_consumed = set()
    restaurants_demand = set()
    frequency_days = set()

    with open(path_to_file) as csvfile:
        readfile = csv.reader(csvfile, delimiter=",")
        for row in readfile:
            if row[0] == "maria":
                list.append(row[1])
            if row[0] == "arnaldo" and row[1] == "hamburguer":
                total_hamburgers += 1
            if row[0] == "joao":
                total_dishes.add(row[1])
                frequency_days.add(row[2])

            restaurants_demand.add(row[2])
            dishes_consumed.add(row[1])

    result_list = collections.Counter(list).most_common(1)[0][0]
    result_dishes = dishes_consumed.difference(total_dishes)
    result_demand = restaurants_demand.difference(frequency_days)

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{result_list}\n"
            f"{total_hamburgers}\n"
            f"{result_dishes}\n"
            f"{result_demand}"
        )


analyze_log("data/orders_1.csv")
