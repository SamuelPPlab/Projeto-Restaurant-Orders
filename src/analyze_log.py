import csv


def arnaldo_ask_hamburguer(orders, user):
    count = 0
    for row in orders:
        if row[0] == user:
            if row[1] == "hamburguer":
                count += 1
    return count


def maria_eats(orders, user):
    count = {}
    most_frequent = 0
    food = ""
    for row in orders:
        if row[0] == user:
            if row[1] not in count:
                count[row[1]] = 1
            else:
                count[row[1]] += 1
            if count[row[1]] > most_frequent:
                most_frequent = count[row[1]]
                food = row[1]
    return food


def joao_never_ask(orders, user):
    foods = set()
    days = set()
    count_foods = set()
    count_days = set()
    for a, b, c in orders:
        if a == user:
            count_foods.add(b)
            count_days.add(c)
        foods.add(b)
        days.add(c)
    return_foods = foods.symmetric_difference(count_foods)
    return_days = days.symmetric_difference(count_days)
    return return_foods, return_days


def analyze_log(path_to_file):
    try:
        with open(path_to_file, mode="r") as file_csv:
            orders = [row for row in csv.reader(file_csv)]
            maria_eats_log = maria_eats(orders, "maria")
            arnaldo_ask_hamburguer_log = arnaldo_ask_hamburguer(
                orders, "arnaldo"
            )
            joao_never_ask_log = joao_never_ask(orders, "joao")
    except ValueError:
        raise FileNotFoundError(f"No such file or directory: {path_to_file}")

    with open("data/mkt_campaign.txt", mode="w+") as file_txt:
        file_txt.write(f"{str(maria_eats_log)}\n")
        file_txt.write(f"{str(arnaldo_ask_hamburguer_log)}\n")
        file_txt.write(f"{str(joao_never_ask_log)}\n")


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
