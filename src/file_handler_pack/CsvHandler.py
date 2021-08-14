from src.file_handler_pack.Handler import Handler
import csv


class CsvHandler(Handler):
    @staticmethod
    def read(file_name: str, delimiter: str = ","):
        with open(file_name, "r") as csvfile:
            return [
                tuple(item)
                for item in csv.reader(csvfile, delimiter=delimiter)
            ]

    @staticmethod
    def writer(texts: list[str], file_name: str):
        with open(file_name, "w") as csvfile:
            writer_in = csv.writer(
                csvfile,
                delimiter=",",
                escapechar=" ",
                quoting=csv.QUOTE_NONE,
            )
            for line in texts:
                writer_in.writerow([line])
