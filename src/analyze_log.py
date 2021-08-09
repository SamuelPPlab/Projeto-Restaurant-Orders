import csv


def maria_favorite_helper(maria):
    maria_favorite = ""
    for key in maria.keys():
        if maria_favorite == "":
            maria_favorite = key
        if maria[key] > maria[maria_favorite]:
            maria_favorite = key
    return str(maria_favorite)


def maria_favorite(path_to_file):
    with open(path_to_file) as file:
        file = csv.reader(file, delimiter=",", quotechar='"')
        maria = {}
        for line in file:
            if line[0] == "maria":
                if line[1] in maria.keys():
                    maria[line[1]] += 1
                else:
                    maria[line[1]] = 1

        return maria_favorite_helper(maria)


def joao_ask(path_to_file):
    with open(path_to_file) as file:
        file = csv.reader(file, delimiter=",", quotechar='"')
        joao_asked = set()
        joao_not_asked = set()
        for line in file:
            if line[0] == "joao":
                joao_asked.add(line[1])
            else:
                joao_not_asked.add(line[1])

        return str(joao_not_asked - joao_asked)


def joao_arrive(path_to_file):
    with open(path_to_file) as file:
        file = csv.reader(file, delimiter=",", quotechar='"')
        joao_came = set()
        joao_didt_come = set()

        for line in file:
            # joao came
            if line[0] == "joao":
                joao_came.add(line[2])
            else:
                joao_didt_come.add(line[2])
        return str(joao_didt_come - joao_came)


def arnaldo_hamburger_count(path_to_file):
    with open(path_to_file) as file:
        file = csv.reader(file, delimiter=",", quotechar='"')
        arnaldo_hamburguer_count = 0
        for line in file:
            if line[0] == "arnaldo" and line[1] == "hamburguer":
                arnaldo_hamburguer_count += 1
        return str(arnaldo_hamburguer_count)


def analyze_log(path_to_file):
    Vmaria_favorite = maria_favorite(path_to_file) + "\n"
    Varnaldo = arnaldo_hamburger_count(path_to_file) + "\n"
    Vjoao_ask = joao_ask(path_to_file) + "\n"
    Vjoao_arrive = joao_arrive(path_to_file)

    f = open("data/mkt_campaign.txt", "w")
    f.write(Vmaria_favorite + Varnaldo + Vjoao_ask + Vjoao_arrive)
    f.close()


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
