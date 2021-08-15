import csv
from collections import Counter


def demanded(name_client, dishes, wish_list):
    ordered_dishes = [
        request["dishes"]
        for request in wish_list
        if request["name_client"] == name_client
    ]
    count = Counter(ordered_dishes)
    demanded = count.get(dishes)
    return demanded


def create_wish_list(path_to_file):
    with open(path_to_file, "r") as file:
        keys = ["name_client", "dishes", "days"]
        dic_dishes = csv.DictReader(file, fieldnames=keys)
        wish_list = []
        [wish_list.append(request) for request in dic_dishes]
    return wish_list


def days_not_go(name_client, list_request):
    every_day = {request["days"] for request in list_request}
    days_go = {
        request["days"]
        for request in list_request
        if request["name_client"] == name_client
    }
    days_not_go = every_day.symmetric_difference(days_go)
    return days_not_go


def most_requested_dishes(name_client, wish_list):
    ordered_dishes = [
        request["dishes"]
        for request in wish_list
        if request["name_client"] == name_client
    ]
    count = Counter(ordered_dishes)
    most_requested_dishes = count.most_common(1)[0][0]
    return most_requested_dishes

def ordered_not_dishes(name_client, list_request):
    every_dish = {request["dishes"] for request in list_request}
    ordered_dishes = {
        request["dishes"]
        for request in list_request
        if request["name_client"] == name_client
    }
    ordered_not_dishes = every_dish.symmetric_difference(ordered_dishes)
    return ordered_not_dishes

def analyze_log(path_to_file):
    if path_to_file.endswith(".csv"):
        text_file = "data/mkt_campaign.txt"
        wish_list = create_wish_list(path_to_file)
        most_requested_dishes_maria = most_requested_dishes("maria", wish_list)
        demanded_hamburguer_arnaldo = demanded(
            "arnaldo", "hamburguer", wish_list
        )
        ordered_not_dishes_joao = ordered_not_dishes("joao", wish_list)
        days_not_go_joao = days_not_go("joao", wish_list)
        content_file = [
            f"{most_requested_dishes_maria}\n",
            f"{demanded_hamburguer_arnaldo}\n",
            f"{ordered_not_dishes_joao}\n",
            f"{days_not_go_joao}",
        ]
        with open(text_file, "w") as file:
            file.writelines(content_file)
    else:
        raise FileNotFoundError(
            f"No such file or directory: '{path_to_file}'"
        )


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
