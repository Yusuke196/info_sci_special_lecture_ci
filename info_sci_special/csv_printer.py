import csv


class CSVPrinter:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        if self.file_name.endswith('tsv'):
            raise Exception('This is TSV')
        elif self.file_name.endswith('txt'):
            raise Exception('This is TXT')

        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
        return lines
