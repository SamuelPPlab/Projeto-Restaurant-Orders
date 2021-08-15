import collections
import csv

orders = set()
days = set()
joao_food = set()
joao_days = set()

maria_orders = []
arnaldo_attendance = 0


def analyze_log(path):
    text = "No such file or directory: " "'data/orders_1.txt'"
    if path.endswith(".csv"):
        with open(path) as file:

            read_file = csv.reader(file, delimiter=",")
            analyze(read_file)

    else:
        raise FileNotFoundError(text)


def analyze(file):
    arnaldo_attendance = 0

    for line in file:

        if(line[0] == "maria"):
            maria_orders.append(line[1])
        if(line[0] == "arnaldo" and line[1] == "hamburguer"):
            arnaldo_attendance += 1
        if(line[0] == "joao"):
            joao_food.add(line[1])
            joao_days.add(line[2])

        orders.add(line[1])
        days.add(line[2])

    favorite_dish = collections.Counter(maria_orders).most_common(1)[0][0]
    joao_never_order = orders.difference(joao_food)
    joao_doesnt_go = days.difference(joao_days)

    final_file = f"{favorite_dish}\n"
    final_file += f"{arnaldo_attendance}\n"
    final_file += f"{joao_never_order}\n"
    final_file += f"{joao_doesnt_go}\n"

    f = open("data/mkt_campaign.txt", "w")
    f.write(final_file)
    f.close()
