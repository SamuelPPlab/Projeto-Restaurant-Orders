import csv


def reader_csv(path_to_file):
    try:
        with open(path_to_file) as file:
            csv_reader = csv.reader(file, delimiter=",", quotechar='"')
            return list(csv_reader)
    except Exception:
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
