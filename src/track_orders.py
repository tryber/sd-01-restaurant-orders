from service import greater_value, group_type, cont_specify_item, not_in_arr, show_values, list_plate, list_days


class TrackOrders:
    def __init__(self):
        self._orders = []

    def add_new_order(self, costumer, order, day):
        costumer_order = dict(costumer=costumer, order=order, day=day)
        self._orders.append(costumer_order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return greater_value(group_type(self._orders, costumer, 'costumer'), 'order')

    def get_order_frequency_per_costumer(self, costumer, order):
        return cont_specify_item(group_type(self._orders, costumer, 'costumer'), 'order', order)

    def get_never_ordered_per_costumer(self, costumer):
        return not_in_arr(list_plate, show_values(group_type(self._orders, costumer, 'costumer'), 'order'))

    def get_days_never_visited_per_costumer(self, costumer):
        return not_in_arr(list_days, show_values(group_type(self._orders, costumer, 'costumer'), 'day'))
