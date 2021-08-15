def different_data(person, list_foods, data_type):
    person_data = {}
    others_data = {}
    index = None

    if data_type == "food":
        index = 1
    else:
        index = 2

    for people in list_foods:
        if people[0] == person:
            set_data = set(person_data)
            person_data = set_data.union({people[index]})
        elif people[index] not in others_data:
            others_data[people[index]] = 1
        else:
            others_data[people[index]] += 1

    others_data = set(others_data)

    return f"{person_data ^ others_data}\n"
