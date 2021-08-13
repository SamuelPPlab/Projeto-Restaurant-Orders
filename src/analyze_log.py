def create_log_dict(file_list):
    log_dict = {}
    menu = set()
    week_days = set()

    for order in file_list:
        order_list = order.split(',')
        menu = menu.union({ order_list[1] })
        week_days = week_days.union({ order_list[2] })

        if order_list[0] not in log_dict:
            log_dict[order_list[0]] = {
                'dishes': {
                    order_list[1]: 1
                },
                'visit_days': set([order_list[2]])
            }
        elif order_list[1] in log_dict[order_list[0]]['dishes']:
            log_dict[order_list[0]]['dishes'][order_list[1]] += 1
            log_dict[order_list[0]]['visit_days'] = log_dict[order_list[0]]['visit_days'].union(set([order_list[2]]))
        else:
            log_dict[order_list[0]]['dishes'][order_list[1]] = 1
            log_dict[order_list[0]]['visit_days'] = log_dict[order_list[0]]['visit_days'].union(set([order_list[2]]))

    return [log_dict, menu, week_days]

def get_most_required_dish(customer_name, log):
    biggest_number = 0
    dish_name = ''

    for dish, value in log[customer_name]['dishes'].items():
        if value > biggest_number:
            dish_name = dish
            biggest_number = value

    return dish_name

def analyze_log(path_to_file):
    log_dict = {}
    response_list = []
    menu = {}
    week_days = {}

    with open(path_to_file) as file:
        file_list = file.read().split('\n')
        log_dict = create_log_dict(file_list)[0]
        menu = create_log_dict(file_list)[1]
        week_days = create_log_dict(file_list)[2]
    

    response_list.append(get_most_required_dish('maria', log_dict))
    response_list.append(log_dict['arnaldo']['dishes']['hamburguer'])
    response_list.append(menu.difference(set(log_dict['joao']['dishes'].keys())))
    response_list.append(week_days.difference(log_dict['joao']['visit_days']))
    
    with open('data/mkt_campaign.txt', 'w') as file_data:
        for response in response_list:
            file_data.write(f'{response}\n')

analyze_log('data/orders_1.csv')
