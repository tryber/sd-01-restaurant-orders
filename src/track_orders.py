from serv.service import Services

func_services = Services()


class TrackOrders:
    def __init__(self):
        self._orders = []

    def add_new_order(self, costumer, order, day):
        costumer_order = dict(costumer=costumer, order=order, day=day)
        self._orders.append(costumer_order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return func_services.greater_value(func_services.group_type(self._orders, costumer, 'costumer'), 'order')

    def get_order_frequency_per_costumer(self, costumer, order):
        return func_services.cont_specify_item(func_services.group_type(self._orders, costumer, 'costumer'), 'order', order)

    def get_never_ordered_per_costumer(self, costumer):
        return func_services.not_in_arr(func_services.list_plate, func_services.show_values(func_services.group_type(self._orders, costumer, 'costumer'), 'order'))

    def get_days_never_visited_per_costumer(self, costumer):
        return func_services.not_in_arr(func_services.list_days, func_services.show_values(func_services.group_type(self._orders, costumer, 'costumer'), 'day'))

    def get_busiest_day(self):
        return func_services.greater_value(self._orders, 'day')

    def get_least_busy_day(self):
        return func_services.array_lasted(func_services.cont_itens_all(self._orders, 'day'))
