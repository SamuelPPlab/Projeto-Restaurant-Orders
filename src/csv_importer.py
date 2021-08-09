import csv
from src.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".csv"):
            raise FileNotFoundError(f"No such file or directory: '{path}'")

        with open(path, newline="") as csv_file:
            reader = csv.reader(csv_file)
            data = list(data for data in reader)
        return data
