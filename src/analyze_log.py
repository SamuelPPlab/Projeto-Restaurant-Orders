import csv

def create_txt(name, content):
    try:
        file = open("data/{}".format(name), 'r+')
        file.writelines(content)
    except FileNotFoundError:
        file = open("data/{}".format(name), 'w+')
        file.writelines(content)
    file.close()

def day_of_week(list_days):
    days = ['segunda-feira','terça-feira','sabado']
    list_days_joao = list(item[2] for item in list_days )
    result = {item for item in days if item not in list_days_joao}
    return result


def analyze_log(path_to_file):
    if ".csv" not in path_to_file:
        raise FileNotFoundError ("No such file or directory: " "'{}'".format(path_to_file))
    else:
        with open(path_to_file) as csvfile:
            maria_request = []
            arnaldo_request = []
            joao_request = []
            count = 0
            doc_reader =  csv.reader(csvfile)
            data_csv = list((item for item in doc_reader))
            for request in data_csv:
                if request[0] == 'maria':
                    maria_request.append(request[1])
                if request[0] == 'arnaldo':
                    arnaldo_request.append(request)
                    if request[1] == 'hamburguer':
                        count += 1
                if request[0] == 'joao':
                    joao_request.append(request)
            
            list_food2 = list(item[1] for item in arnaldo_request)
            list_food = maria_request + list_food2
            list_food_joao = list(item[1] for item in joao_request )
            never_request = {item for item in sorted(set(list_food)) if item not in list_food_joao}
            request_maria_max = max(set(maria_request), key=maria_request.count)

                      
            create_txt('mkt_campaign.txt', f"{request_maria_max}\n{count}\n{never_request}\n{day_of_week(joao_request)}") 


print(analyze_log("data/orders_1.csv"))