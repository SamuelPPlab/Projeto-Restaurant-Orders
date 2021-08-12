import csv


def analyze_log(path_to_file):
    listOrder = import_csv(path_to_file)
    dict = {}
    for order in listOrder:
        if order[0] not in dict:
            dict[order[0]] = {
                "foods": {
                    "hamburguer": 0,
                    "pizza": 0,
                    "coxinha": 0,
                    "misto-quente": 0,
                },
                "dayList": {
                    "segunda-feira": 0,
                    "terça-feira": 0,
                    "quarta-feira": 0,
                    "quinta-feira": 0,
                    "sexta-feira": 0,
                    "sabado": 0,
                    "domingo": 0,
                },
            }
        if order[1] not in dict[order[0]]["foods"]:
            dict[order[0]]["foods"][order[1]] = 1
        else:
            dict[order[0]]["foods"][order[1]] += 1
        dict[order[0]]["dayList"][order[2]] += 1

    bestFoodMaria = max(dict["maria"]["foods"], key=dict["maria"]["foods"].get)
    hamburguerArnaldo = dict["arnaldo"]["foods"]["hamburguer"]
    clientDictDay = dict["joao"]["dayList"]
    foodJoao = dict["joao"]["foods"]
    joaoNotOrder = {key for key in foodJoao if foodJoao[key] == 0}
    joaoNotGo = {key for key in clientDictDay if clientDictDay[key] == 0}
    print(joaoNotGo)
    result = f"{bestFoodMaria}\n{hamburguerArnaldo}\n"
    result = result + f"{joaoNotOrder}\n{joaoNotGo}"
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(result)


def import_csv(path):
    with open(path, "r") as file:
        dictionaty = csv.reader(file, delimiter=",", quotechar='"')
        return [row for row in dictionaty]


if __name__ == "__main__":
    analyze_log("./data/orders_2.csv")
