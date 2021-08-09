import collections
import csv


def analyze_log(path_to_file):
    m_orders = []
    orders = set()
    days = set()
    arnaldo_counter = 0
    joao_orders = set()
    joao_days = set()
    answers = ""

    with open(path_to_file) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",")
        for line in spamreader:
            orders.add(line[1])
            days.add(line[2])
            if line[0] == "maria":
                m_orders.append(line[1])
            if line[0] == "arnaldo" and line[1] == "hamburguer":
                arnaldo_counter += 1
            if line[0] == "joao":
                joao_orders.add(line[1])
                joao_days.add(line[2])
        answers += f"{collections.Counter(m_orders).most_common(1)[0][0]}\n"
        answers += f"{arnaldo_counter}\n"
        answers += f"{orders.difference(joao_orders)}\n"
        answers += f"{days.difference(joao_days)}"

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(answers)
