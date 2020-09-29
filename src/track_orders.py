class TrackOrders:
    def __init__(self):
        self._data = []

    def add_new_order(self, costumer, order, day):
        self._data.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_frequent_food = self._data[0][1]
        frequency = {}

        for food in self._data:

            index_food = food[1]

            if index_food not in frequency:
                frequency[index_food] = 1

            else:
                frequency[index_food] += 1

            if frequency[index_food] > frequency[most_frequent_food]:
                most_frequent_food = index_food

        return f"Prato favorito do(a) cliente {costumer}: {most_frequent_food}"

    def get_order_frequency_per_costumer(self, costumer, order):
        frequency = {'hamburguer': 0, 'pizza': 0, 'coxinha': 0, 'misto-quente': 0}

        for food in self._data:
            index_food = food[1]
            frequency[index_food] += 1

        return f"Quantidade de pedidos de {order} feito pelo/a cliente {costumer}: {frequency[order]}"

    def get_never_ordered_per_costumer(self, costumer):
        frequency = set()
        products = set({'hamburguer', 'pizza', 'coxinha', 'misto-quente'})

        for food in self._data:
            frequency.add(food[1])
        
        if products == frequency:
            return f"O/A cliente {costumer} pediu todos os pedidos"

        return f"Pedido nunca pedido pelo(a) cliente {self._data[0][0]}: {products.difference(frequency)}"

    def get_days_most_visited_per_costumer(self, costumer):
        present_days = []
        days = ['segunda-feira', 'terça-feira', 'sabado']
        days_set = set(days)

        for food in self._data:
            present_days.append(food[2])

        present_days_set = set(present_days)
        return f"Dia(s) mais visitado(s) pelo(a) cliente {costumer}: {days_set.intersection(present_days_set)}"

    def get_days_never_visited_per_costumer(self, costumer):
        present_days = []
        days = ['segunda-feira', 'terça-feira', 'sabado']
        days_set = set(days)

        for food in self._data:
            present_days.append(food[2])

        present_days_set = set(present_days)

        if present_days_set == days_set:
            return f"O/A cliente {costumer} comparece em todos os dias"

        return f"Dia(s) menos visitado(s) pelo(a) cliente {self._data[0][0]}: {days_set.difference(present_days_set)}"
