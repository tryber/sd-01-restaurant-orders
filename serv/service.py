import csv

list_plate = ['hamburguer', 'pizza', 'misto-quente', 'coxinha']
list_client = ['maria', 'joao', 'arnaldo']
list_days = ['segunda-feira', 'quarta-feira', 'terça-feira', 'quinta-feira', 'sexta-feira', 'domingo', 'sabado']


class Services:
    def __init__(self):
        self.list_plate = list_plate
        self.list_client = list_client
        self.list_days = list_days

    def import_data(self, path):
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            return [row for row in csv_reader]

    def group_type(self, data, value, type_filter):
        return list(filter(lambda order: order[type_filter] == value, data))

    def cont_itens_all(self, data, type_filter):
        frequency = {}
        for value in data:
            if value[type_filter] not in frequency:
                frequency[value[type_filter]] = 1
            else:
                frequency[value[type_filter]] += 1
        return frequency
    
    def array_lasted(self, data):
        return min(data)

    def get_set(self, value):
        return {'day': self.list_days, 'plate': self.list_plate, 'client': self.list_client}[value]

    def not_in_arr(self, verify, comparision):
        set_verify = set(verify)
        set_comparision = set(comparision)
        return set_verify.difference(set_comparision)

    def show_values(self, data, type_filter):
        values = []
        for value in data:
            if value[type_filter] not in values:
                values.append(value[type_filter])
        return values

    def greater_value(self, data, type_filter):
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

    def cont_specify_item(self, data, type_filter, value):
        if value not in self.cont_itens_all(data, type_filter):
            return [value, 0]
        return self.cont_itens_all(data, type_filter)[value]

    def write_file(self, name, data):
        with open(name, 'w', encoding='utf-8-sig') as file:
            for value in data:
                file.write(value+'\n')
