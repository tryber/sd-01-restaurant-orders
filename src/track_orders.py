class TrackOrders:
    # def add_new_order(self, costumer, order, day):
    #     pass

    def get_most_ordered_dish_per_costumer(self, costumer, filter_data):
        most_frequent_food = filter_data[0][1]
        frequency = {}

        for food in filter_data:

            index_food = food[1]

            if index_food not in frequency:
                frequency[index_food] = 1

            else:
                frequency[index_food] += 1

            if frequency[index_food] > frequency[most_frequent_food]:
                most_frequent_food = index_food

        return f"Prato favorito do(a) cliente {costumer}: {most_frequent_food}"

    def get_order_frequency_per_costumer(self, costumer, order, filter_data):
        frequency = {'hamburguer': 0, 'pizza': 0, 'coxinha': 0, 'misto-quente': 0}

        for food in filter_data:
            index_food = food[1]
            frequency[index_food] += 1

        return f"Pedido mais frequente do(a) cliente {costumer}: {frequency[order]}"

    def get_never_ordered_per_costumer(self, filter_data):
        frequency = set()
        products = set({'hamburguer', 'pizza', 'coxinha', 'misto-quente'})

        for food in filter_data:
            frequency.add(food[1])

        return f"Pedido nunca pedido pelo(a) cliente {filter_data[0][0]}: {products.difference(frequency)}"

    def get_days_most_visited_per_costumer(self, filter_data):
        present_days = []
        days = ['segunda-feira', 'terça-feira', 'sabado']
        days_set = set(days)

        for food in filter_data:
            present_days.append(food[2])

        present_days_set = set(present_days)
        return f"Dia(s) mais visitado(s) pelo(a) cliente {filter_data[0][0]}: {days_set.intersection(present_days_set)}"

    def get_days_never_visited_per_costumer(self, filter_data):
        present_days = []
        days = ['segunda-feira', 'terça-feira', 'sabado']
        days_set = set(days)

        for food in filter_data:
            present_days.append(food[2])

        present_days_set = set(present_days)
        return f"Dia(s) menos visitado(s) pelo(a) cliente {filter_data[0][0]}: {days_set.difference(present_days_set)}"
