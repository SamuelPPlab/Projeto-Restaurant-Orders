from csv import DictReader
import os


def read_data(path):
    if not path.endswith(".csv") or not os.path.isfile(path):
        raise FileNotFoundError(f"No such file or directory: '{path}'")
    with open(path, "r") as csv_file:
        fieldnames = ["client", "order", "day"]
        reader = DictReader(csv_file, fieldnames=fieldnames)
        data = list(row for row in reader)
    return data


def analyze_log(path_to_file):
    data = read_data(path_to_file)
    return data
