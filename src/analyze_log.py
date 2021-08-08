import csv


class AnalyzeDataByPerson:
    def __init__(
        self,
        list_orders: list,
        dishes: set = {"hamburguer", "pizza", "coxinha", "misto-quente"},
    ) -> None:
        self.list_orders = list_orders
        self.dishes = dishes

    def most_ordered_dish(self, name):
        # print(list_orders)
        client_orders = {}
        for info in self.list_orders:
            if info["name"] == name:
                if info["order"] not in client_orders:
                    client_orders[info["order"]] = 1
                else:
                    client_orders[info["order"]] += 1
        return list(client_orders.keys())[0]

    def times_ordered_dish(self, name, order):
        counter = 0
        for info in self.list_orders:
            if info["name"] == name and info["order"] == order:
                counter += 1
        return counter

    def dishes_never_ordered(self, name):
        dishes_ordered = set()
        for info in self.list_orders:
            if info["name"] == name:
                dishes_ordered.add(info["order"])
        return self.dishes.difference(dishes_ordered)

    def days_not_present(self, name):
        days = {
            "segunda-feira",
            "terça-feira",
            "sabado"
        }
        days_present = set()
        for info in self.list_orders:
            if info["name"] == name:
                days_present.add(info["day"])

        return days.difference(days_present)


def analyze_log(path_to_file):
    # with open(path_to_file) as csvfile:
    #     spamreader = csv.reader(csvfile, delimiter=",")
    #     for row in spamreader:
    #         print(row)
    with open(path_to_file, "r") as file:
        dict_reader = list(
            csv.DictReader(file, fieldnames=["name", "order", "day"])
        )
        analyzeData = AnalyzeDataByPerson(dict_reader)

        with open("data/mkt_campaign.txt", "w") as write_file:
            print(
                analyzeData.most_ordered_dish("maria"),
                analyzeData.times_ordered_dish("arnaldo", "hamburguer"),
                analyzeData.dishes_never_ordered("joao"),
                analyzeData.days_not_present("joao"),
                sep="\n",
                file=write_file,
            )


analyze_log("data/orders_1.csv")
