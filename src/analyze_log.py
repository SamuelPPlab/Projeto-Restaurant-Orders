# Funções implementadas separadamente
from src.functions.fun_analyze import most_frequent_item
from src.functions.fun_analyze import days_person_not_go_cafeteria
from src.functions.fun_analyze import dishes_never_ordered_per_person
from src.functions.fun_analyze import number_of_dishes_per_person
from src.functions.fun_analyze import read_csv_to_list


def analyze_log(path_to_file):
    orders = read_csv_to_list(path_to_file)

    client_dishes = dict()
    client_days = dict()
    menu = set()
    days_of_week = set()

    for order in orders:
        menu.add(order[1])
        days_of_week.add(order[2])
        client_dishes[order[0]] = client_dishes.get(order[0], []) + [order[1]]
        client_days[order[0]] = client_days.get(order[0], []) + [order[2]]

    most_frequent_dishe_maria = most_frequent_item(
        client_dishes["maria"]
    )
    quantity_arnaldo_hamburguer = number_of_dishes_per_person(
        client_dishes["arnaldo"], "hamburguer"
    )

    dishes_never_ordered_by_joao = dishes_never_ordered_per_person(
        menu, client_dishes["joao"]
    )

    days_joao_not_go_to_cafeteria = days_person_not_go_cafeteria(
        days_of_week, client_days["joao"]
    )

    with open("data/mkt_campaign.txt", mode="w") as mkt_campaign:
        mkt_campaign.write(
            f"{most_frequent_dishe_maria}\n"
            f"{quantity_arnaldo_hamburguer}\n"
            f"{dishes_never_ordered_by_joao}\n"
            f"{days_joao_not_go_to_cafeteria}"
        )


# print(
#     analyze_log(
#         "/home/vanderson/Trybe/projetos_trybe/BLOCO_38_T6/sd-06-restaurant-orders/data/orders_1.csv"
#     )
# )
