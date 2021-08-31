import csv


def file_importer(path_to_file):
    log = []
    with open(path_to_file) as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            entry = {}
            entry['cliente'] = row[0]
            entry['pedido'] = row[1]
            entry['dia'] = row[2]
            log.append(entry)
    return log

def analyze_log(path_to_file):
    log = file_importer(path_to_file)
    pedidos_de_maria = []
    for item in log:
        if (item['cliente'] == 'maria'):
            pedidos_de_maria.append(item['pedido'])
    pedidos_de_maria
    print(pedidos_de_maria)

analyze_log("data/orders_1.csv")