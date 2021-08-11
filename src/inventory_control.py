class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.ingredients_balance = self.MINIMUM_INVENTORY.copy()

    def add_new_order(self, _customer, order, _day):
        ingredients = self.INGREDIENTS[order]

        for ingredient in ingredients:
            if self.ingredients_balance[ingredient] == 0:
                return False

            self.ingredients_balance[ingredient] -= 1

    def get_quantities_to_buy(self):
        balance_report = dict()

        for ingredient in self.ingredients_balance:
            balance = (
                self.MINIMUM_INVENTORY[ingredient]
                - self.ingredients_balance[ingredient]
            )

            balance_report[ingredient] = balance

        return balance_report

    def get_available_dishes(self):
        available_dishes = set()

        for dish in self.INGREDIENTS:
            ingredients = self.INGREDIENTS[dish]

            has_enough = True

            for ingredient in ingredients:
                if self.ingredients_balance[ingredient] == 0:
                    has_enough = False
                    break

            if has_enough:
                available_dishes.add(dish)

        return available_dishes
