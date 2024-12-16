from pandas import DataFrame

class CsvCreator:
    def __init__(self):
        pass
    def csv_folder(self, data):
        csv_name = "output.csv"
        frame = DataFrame(data)

        frame.to_csv(csv_name)