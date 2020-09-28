import csv


def read_file_csv(file, plate_favorite):
    with open(file) as csv_file:
        filter_person = []
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if row[0] == plate_favorite:
                filter_person.append(row)

    return filter_person


def analyse_log(path_to_file):
    raise NotImplementedError
