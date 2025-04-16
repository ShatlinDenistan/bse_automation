import csv


class CSVLibrary:

    def read_csv_file(self, filename):
        """This creates a keyword named "Read CSV File"

        This keyword takes one argument, which is a path to a .csv file. It
        returns a list of rows, with each row being a list of the data in
        each column.
        """
        data = []
        try:
            with open(filename, "r", encoding="utf-8", newline="") as csvfile:
                reader = csv.reader(csvfile, delimiter=",", dialect="excel")
                for row in reader:
                    for i in row:
                        data.append(i)
            return data
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"CSV file not found: {filename}") from exc
        except (csv.Error, OSError) as exc:
            raise IOError(f"Error reading CSV file: {str(exc)}") from exc

    def clear_file(self, filepath):
        try:
            with open(filepath, "w", encoding="utf-8", newline="") as csvfile:
                csv.writer(csvfile)
        except (csv.Error, OSError) as exc:
            raise IOError(f"Error clearing CSV file: {str(exc)}") from exc

    def append_file(self, filepath, data):
        try:
            with open(filepath, "a", encoding="utf-8", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data)
        except (csv.Error, OSError) as exc:
            raise IOError(f"Error appending to CSV file: {str(exc)}") from exc
