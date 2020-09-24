class TrackOrders:
    def __init__(self):
        self.data = []
        self.days = set(
            [
                "segunda-feira",
                "terça-feira",
                "quarta-feira",
                "quinta-feira",
                "sexta-feira",
                "sabado",
                "domingo",
            ]
        )

    def add_new_order(self, costumer, order, day):
        self.data.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        client_and_dishe_favoricted = {}
        most_frequent = 0
        for elements in self.data:
            if elements[0] == costumer:
                if elements[1] in client_and_dishe_favoricted:
                    client_and_dishe_favoricted[elements[1]] += 1
                else:
                    client_and_dishe_favoricted[elements[1]] = 1
                if client_and_dishe_favoricted[elements[1]] > most_frequent:
                    most_frequent = client_and_dishe_favoricted[elements[1]]
        return most_frequent

    def get_dish_quantity_per_costumer(self, costumer, order):
        new_dict = {}
        most_frequent = 0
        for elements in self.data:
            if elements[0] == costumer and elements[1] == order:
                if elements[1] in new_dict:
                    new_dict[elements[1]] += 1
                else:
                    new_dict[elements[1]] = 1
                if new_dict[elements[1]] > most_frequent:
                    most_frequent = new_dict[elements[1]]
        return most_frequent

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = self.get_all_orderes()
        costumer_orders = set()
        for element in self.data:
            if element[0] == costumer:
                costumer_orders.add(element[1])
        return all_orders.difference(costumer_orders)

    def get_busiest_day(self):
        new_dict = {}
        most_frequent = 0
        dish_name = ''
        for elements in self.data:
            if elements[2] in new_dict:
                new_dict[elements[2]] += 1
            else:
                new_dict[elements[2]] = 1
            if new_dict[elements[2]] > most_frequent:
                most_frequent = new_dict[elements[2]]
                dish_name = elements[2]
        return dish_name

    def get_least_busy_day(self):
        new_dict = {}
        for elements in self.data:
            if elements[2] in new_dict:
                new_dict[elements[2]] += 1
            else:
                new_dict[elements[2]] = 1
        return min(new_dict, key=new_dict.get)

    def get_all_orderes(self):
        new_set = set()
        for element in self.data:
            new_set.add(element[1])
        return new_set
