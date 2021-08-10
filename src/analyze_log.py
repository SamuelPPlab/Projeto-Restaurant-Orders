import collections
import csv

orders = set()
days = set()
maria_orders = []
arnaldo_frequency = 0
joao_dishes = set()
joao_days = set()


def analyze_log(path):
    expect_text = "No such file or directory: " "'data/orders_1.txt'"
    if path.endswith(".csv"):
        with open(path) as file:

            read_file = csv.reader(file, delimiter=",")
            analyze(read_file)

    else:
        raise FileNotFoundError(expect_text)


def analyze(file):
    arnaldo_frequency = 0

    for line in file:

        if(line[0] == "maria"):
            maria_orders.append(line[1])
        if(line[0] == "arnaldo" and line[1] == "hamburguer"):
            arnaldo_frequency += 1
        if(line[0] == "joao"):
            joao_dishes.add(line[1])
            joao_days.add(line[2])

        orders.add(line[1])
        days.add(line[2])

    most_common_dishe = collections.Counter(maria_orders).most_common(1)[0][0]
    joao_never_ask = orders.difference(joao_dishes)
    joao_never_go = days.difference(joao_days)

    final_file = f"{most_common_dishe}\n"
    final_file += f"{arnaldo_frequency}\n"
    final_file += f"{joao_never_ask}\n"
    final_file += f"{joao_never_go}\n"

    f = open("data/mkt_campaign.txt", "w")
    f.write(final_file)
    f.close()
