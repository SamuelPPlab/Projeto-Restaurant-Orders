import csv
import os.path


def analyze_log(path_to_file):
    document_type = path_to_file[-3:]
    if document_type != "csv":
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    if os.path.exists(path_to_file) is False:
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    report_list = []
    with open(path_to_file, mode="r") as file:
        report_reader = csv.DictReader(file)
        for row in report_reader:
            report_list.append(row)
    return report_list


print(analyze_log("data/orders_1.csv"))
