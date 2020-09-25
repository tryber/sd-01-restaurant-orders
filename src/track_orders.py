class TrackOrders:
    def __init__(self):
        self._array = list()

    # def _writer(self, path, file):
    #     with open(path, "a") as txt_file:
    #         txt_file.write(file)
    #     return txt_file.close()

    def __factory(self, key, client):
        all_customers = self._array

        def __filter(x):
            return x["costumer"] == client

        return {
            "all": list(set([row[key] for row in all_customers])),
            "client": list(filter(__filter, all_customers)),
        }

    def __most_frequent_client(self, client):

        most_frequent_lunch = client[0]["order"]
        frequency = {}
        for lunch in client:
            if lunch["order"] not in frequency:
                frequency[lunch["order"]] = 1
            else:
                frequency[lunch["order"]] += 1

            if frequency[lunch["order"]] > frequency[most_frequent_lunch]:
                most_frequent_lunch = lunch["order"]
        return most_frequent_lunch

    def _frequency_order(self, keys, client):
        frequency = {k: 0 for k in sorted(keys)}
        for all_orders in client:
            if all_orders["order"] not in frequency:
                frequency[all_orders["order"]] = 1
            else:
                frequency[all_orders["order"]] += 1
        return frequency

    def __format_string(self, obj):
        answer = [f"{k}," for k, v in obj.items() if v == 0]
        lenght = len(answer) - 1
        answer_finally = ""
        for index, day in enumerate(answer):
            if index == lenght:
                answer_finally += f" e {day[:-1]}."
            elif index == lenght - 1:
                answer_finally += f"{day[:-1]}"
            else:
                answer_finally += f"{day} "
        return answer_finally

    def add_new_order(self, costumer, order, day):
        costumer_order = dict(costumer=costumer, order=order, day=day)
        self._array.append(costumer_order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        all_customers = self._array

        def __filter(x):
            return x["costumer"] == costumer

        costumer_list = list(filter(__filter, all_customers))

        answer = f"""O prato favorito do/a {costumer.capitalize()} é o:
{self.__most_frequent_client(costumer_list)}"""
        return answer

    def get_order_frequency_per_costumer(self, costumer, order):
        call_factory = self.__factory("order", costumer)
        totally_orders = self._frequency_order(
            call_factory.get("all"), call_factory.get("client")
        )
        if order not in call_factory.get("all"):
            return "O prato não existe!"
        totally_orders = self._frequency_order(
            call_factory.get("all"), call_factory.get("client")
        )
        answer = f"""O/A {costumer.capitalize()} consumiu:
{totally_orders.get(order)} {order} no total"""
        return answer

    def get_never_ordered_per_costumer(self, costumer):
        call_factory = self.__factory("order", costumer)
        totally_orders = self._frequency_order(
            call_factory.get("all"), call_factory.get("client")
        )
        answer = f"""{costumer.capitalize()} nunca pediu:
{self.__format_string(totally_orders)}"""
        return answer

    def get_days_never_visited_per_costumer(self, costumer):
        call_factory = self.__factory("day", costumer)
        totally_orders = self._frequency_order(
            call_factory.get("all"), call_factory.get("client")
        )
        answer = f"""{costumer.capitalize()} nunca foi nos dias:
{self.__format_string(totally_orders)}"""
        return answer


# tester = TrackOrders()

# values = tester.get_order_frequency_per_costumer("jose", "hamburguer")

# print(values)
