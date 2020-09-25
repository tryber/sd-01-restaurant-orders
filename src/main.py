import csv
from pubsub import pub
from inventory_control import InventoryControl
from track_orders import TrackOrders


def print_info(tracker, control):
    print("-" * 45)
    print(tracker.get_most_ordered_dish_per_costumer("maria"))
    print("-" * 45)
    print()
    print("-" * 45)
    print(tracker.get_order_frequency_per_costumer("arnaldo", "hamburguer"))
    print("-" * 45)
    print()
    print("-" * 45)
    print(tracker.get_never_ordered_per_costumer("joao"))
    print("-" * 45)
    print()
    print("-" * 45)
    print(tracker.get_days_never_visited_per_costumer("joao"))
    print("-" * 45)
    print()
    print("-" * 45)
    print(control.get_quantities_to_buy())
    print("-" * 45)


def main():
    topic = "order"
    path = "data/orders_2.csv"

    tracker = TrackOrders()
    control = InventoryControl()
    subs = [tracker.add_new_order, control.add_new_order]

    for sub in subs:
        pub.subscribe(sub, topic)

    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for costumer, order, day in csv_reader:
            pub.sendMessage(topic, costumer=costumer, order=order, day=day)

    print_info(tracker, control)


if __name__ == "__main__":
    main()


# def csv_or_txt_file_reader_or_writer(modifier, path, file):
#     from csv import DictReader

#     def writer():
#         with open(path, "a") as txt_file:
#             txt_file.write(file)
#         return txt_file.close()

#     def reader():
#         with open(path, "r") as csvfile:
#             fieldnames = ["costumer", "order", "day"]
#             reader = DictReader(csvfile, fieldnames=fieldnames)
#             return [row for row in reader]

#     switcher = {"writer": writer, "reader": reader}
#     return switcher.get(modifier, lambda: "método não implementado")()