import csv
from typing import OrderedDict


def open_file(path):
    result = []
    with open(path) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in reader:
            result.append(tuple(row))

    return result


# def analyze_log(path_to_file):
#     seen_before = set()
#     repeated = set()
#     data = open_file(path_to_file)
#     for line in data:
#         if line in seen_before:
#             repeated.add(line)
#         else:
#             seen_before.add(line)
#     print(seen_before)
#     print('\n\n\n')
#     print(repeated)

def analyze_log(path_to_file):

    data = open_file(path_to_file)
    maria = dict((x, data.count(x)) for x in set(data) if 'maria' in x)
    count = {}
    most_frequent = 1
    result = set()
    for line in data:
        if line not in count:
            count[line] = 1
        else:
            count[line] += 1
        if count[line] > most_frequent:
            most_frequent = count[line]
            result.add(line)
    return list(list(result)[0])[1]


result = analyze_log('data/orders_1.csv')
print(result)
