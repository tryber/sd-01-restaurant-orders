import csv
# from pubsub import pub
from inventory_control import InventoryControl
from track_orders import TrackOrders


def print_info(tracker, control, filter_data):
    print(tracker.get_most_ordered_dish_per_costumer('maria', filter_data('maria')))
    print(tracker.get_order_frequency_per_costumer('arnaldo', 'hamburguer', filter_data('arnaldo')))
    print(tracker.get_never_ordered_per_costumer(filter_data('joao')))
    print(tracker.get_days_most_visited_per_costumer(filter_data('joao')))
    print(tracker.get_days_never_visited_per_costumer(filter_data('joao')))
    # print(control.get_quantities_to_buy())


def main():
    # topic = 'order'
    path = "../data/orders_1.csv"

    tracker = TrackOrders()
    control = InventoryControl()

    def filter_data(customer):
        with open(path) as csv_file:
            filter_person = []
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                if row[0] == customer:
                    filter_person.append(row)

        return filter_person

    # subs = [tracker.add_new_order, control.add_new_order]

    # for sub in subs:
    #     pub.subscribe(sub, topic)

    # with open(path) as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     for costumer, order, day in csv_reader:
    #         pub.sendMessage(topic, costumer=costumer, order=order, day=day)

    print_info(tracker, control, filter_data)


if __name__ == "__main__":
    main()
