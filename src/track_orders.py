class TrackOrders:
    def __init__(self):
        self.pedidos = []
    # referência: Luíse Rios

    def __len__(self):
        return len(self.pedidos)

    def add_new_order(self, costumer, order, day):
        return self.pedidos.append([costumer, order, day])

    def organize_pedidos(self, orders):
        relatory = {}
        for lista in orders:
            if lista[0] not in relatory:
                relatory[lista[0]] = {}
                relatory[lista[0]]["comida"] = []
                relatory[lista[0]]["comida"].append(lista[1])
                relatory[lista[0]]["dia"] = []
                relatory[lista[0]]["dia"].append(lista[2])
            else:
                relatory[lista[0]]["comida"].append(lista[1])
                relatory[lista[0]]["dia"].append(lista[2])

        return relatory

    def get_most_ordered_dish_per_costumer(self, costumer):
        pedidos = self.organize_pedidos(self.pedidos)

        contador = {}
        mais_frequente = pedidos[costumer]['comida'][0]

        for comida in pedidos[costumer]['comida']:
            if comida not in contador:
                contador[comida] = 1
            else:
                contador[comida] += 1

        if contador[comida] > contador[mais_frequente]:
            mais_frequente = comida

        return mais_frequente
        # referência: vídeo da Valéria no conteúdo 37.3

    def get_dish_quantity_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        pedidos = self.organize_pedidos(self.pedidos)
        pratos = ['coxinha', 'misto-quente', 'pizza', 'hamburguer']
        nunca_comeu = set()
        for prato in pratos:
            if prato not in pedidos[costumer]['comida']:
                nunca_comeu.add(prato)

        return nunca_comeu

    def get_days_never_visited_per_costumer(self, costumer):
        pedidos = self.organize_pedidos(self.pedidos)
        dias = ['segunda-feira', 'sabado', 'terça-feira']
        nunca_visitou = set()
        for day in dias:
            if day not in pedidos[costumer]['dia']:
                nunca_visitou.add(day)

        return nunca_visitou

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
