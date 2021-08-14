import csv


def count_most_ordered(list_meals):
    count = {}
    most_ordered = list_meals[0]

    for meal in list_meals:
        if meal not in count:
            count[meal] = 1
        else:
            count[meal] += 1
        if count[meal] > count[most_ordered]:
            most_ordered = meal
    return most_ordered


def count_meal(list_meals, meal_ordered):
    count = {}

    for meal in list_meals:
        if meal not in count:
            count[meal] = 1
        else:
            count[meal] += 1
    return count[meal_ordered]


def analyze_log(path_to_file):
    with open(path_to_file, "r") as file:
        # if not file or not path_to_file.endswith(".csv"):
        #     raise FileNotFoundError("No such file or directory: "
        #         + path_to_file
        #         )
        data = csv.DictReader(file, fieldnames=['name', 'meal', 'day'])
        maria_meals = []
        arnaldo_meals = []
        joao_meals = []
        all_meals = set()
        all_days = set()
        joao_days = set()
        for row in data:
            all_meals.add(row['meal'])
            all_days.add(row['day'])
            if row["name"] == "maria":
                maria_meals.append(row["meal"])
            if row["name"] == "arnaldo":
                arnaldo_meals.append(row["meal"])
            if row["name"] == "joao":
                joao_meals.append(row["meal"])
                joao_days.add(row["day"])

        most_ordered = count_most_ordered(maria_meals)
        count_order = count_meal(arnaldo_meals, "hamburguer")
        set_joao_meals = set(joao_meals)
        joao_never_ask = all_meals - set_joao_meals
        joao_never_go = all_days - joao_days

        to_write = [
            f"{most_ordered}\n",
            f"{count_order}\n",
            f"{joao_never_ask}\n",
            f"{joao_never_go}\n"
        ]
        with open("data/mkt_campaign.txt", "w") as campaign:
            campaign.writelines(to_write)
