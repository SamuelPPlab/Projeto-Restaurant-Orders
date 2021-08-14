from src.file_handler_pack.CsvHandler import CsvHandler
from src.utils.most_request_food import most_request_food
from src.utils.best_counter import count


def analyze_log(path_to_file):
    customer_map = dict()
    foods = set()
    opening_days = set()

    for customer, food, day in CsvHandler.read(path_to_file):
        if customer in customer_map:
            customer_map[customer].append((food, day))
        else:
            customer_map[customer] = [(food, day)]

        foods.add(food)
        opening_days.add(day)

    # Qual o prato mais pedido por 'maria'?
    mary_favorite_food = most_request_food(customer_map["maria"])

    # Quantas vezes 'arnaldo' pediu 'hamburguer'?
    arnaldo_hamburguer_count = count(
        lambda item: True if "hamburguer" in item else False,
        customer_map["arnaldo"],
    )

    # Quais pratos 'joao' nunca pediu?
    john_foods = {food for food, _ in customer_map["joao"]}
    john_did_not_eat = foods.difference(john_foods)

    # Quais dias 'joao' nunca foi na lanchonete?
    john_went_to_the_restaurant = {day for _, day in customer_map["joao"]}
    john_not_went_to_the_restaurant = opening_days.difference(
        john_went_to_the_restaurant
    )

    writer_in_file = [
        mary_favorite_food,
        arnaldo_hamburguer_count,
        john_did_not_eat,
        john_not_went_to_the_restaurant,
    ]

    CsvHandler.writer(writer_in_file, "data/mkt_campaign.txt")


analyze_log("data/orders_1.csv")
