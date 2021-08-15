def favorite_food_person(person, list_foods):
    foods = {}
    result = None
    for people in list_foods:
        if people[0] == person:
            if people[1] not in foods:
                foods[people[1]] = 1
            else:
                foods[people[1]] += 1
    if len(foods) > 0:
        result = f"{sorted(foods, key = foods.get, reverse = True)[0]}\n"
    return result
