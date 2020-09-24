from csv import DictReader

list_plate = ['hamburguer', 'pizza', 'misto-quente', 'coxinha']
list_client = ['maria', 'joao', 'arnaldo']
list_days = ['segunda-feira', 'quarta-feira', 'terça-feira', 'quinta-feira', 'sexta-feira', 'domingo', 'sabado']


def import_data(path):
    if not path.endswith("csv"): 
        raise ValueError("Arquivo invalido")
    data = []
    with open(path, "r", encoding='utf-8-sig') as csv_file:
        field = ['client', 'plate', 'day']
        readCSV = DictReader(csv_file, fieldnames=field)
        for values in readCSV:
            data.append(values)
    return data


def group_type(data, value, type_filter):
    return list(filter(lambda order: order[type_filter] == value, data))


def cont_itens_all(data, type_filter):
    frequency = {}
    for value in data:
        if value[type_filter] not in frequency:
            frequency[value[type_filter]] = 1
        else:
            frequency[value[type_filter]] += 1
    return frequency


def get_set(value):
    return {'day': list_days, 'plate': list_plate, 'client': list_client}[value]


def not_in_arr(verify, comparision):
    set_verify = set(verify)
    set_comparision = set(comparision)
    return set_verify.difference(set_comparision)


def show_values(data, type_filter):
    values = []
    for value in data:
        if value[type_filter] not in values:
            values.append(value[type_filter])
    return values


def greater_value(data, type_filter):
    frequency = {}
    current_item = ''
    current_value = 0
    for value in data:
        if value[type_filter] not in frequency:
            frequency[value[type_filter]] = 1
        else:
            frequency[value[type_filter]] += 1
        if frequency[value[type_filter]] > current_value:
            current_value = frequency[value[type_filter]]
            current_item = value[type_filter]
    return [current_item, current_value]


def cont_specify_item(data, type_filter, value):
    if value not in cont_itens_all(data, type_filter):
        return [value, 0]
    return cont_itens_all(data, type_filter)[value]


def write_file(name, data):
    with open(name, 'w', encoding='utf-8-sig') as file:
        for value in data:
            file.writelines(value+'\n')
