from src.utils.reader_csv import reader_csv
from src.utils.favorite_food import favorite_food_person as favorite_food
from src.utils.quantity_product import quantity_of_products as qtd_products
from src.utils.different_data import different_data as diff_data


def analyze_log(path_to_file):
    analized_res = []
    csv_reader = reader_csv(path_to_file)
    analized_res.append(favorite_food("maria", csv_reader))
    analized_res.append(qtd_products("arnaldo", "hamburguer", csv_reader))
    analized_res.append(diff_data("joao", csv_reader, "food"))
    analized_res.append(diff_data("joao", csv_reader, "day"))
    file_txt = open("data/mkt_campaign.txt", mode="w")
    file_txt.writelines(analized_res)
    file_txt.close()

# print(analyze_log("data/orders_1.csv"))
