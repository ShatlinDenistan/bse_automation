import csv
class csvLibrary(object):

    def read_csv_file(self, filename):
        '''This creates a keyword named "Read CSV File"

        This keyword takes one argument, which is a path to a .csv file. It
        returns a list of rows, with each row being a list of the data in 
        each column.
        '''
        data = []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', dialect='excel')
            for row in reader:
                for i in row:
                    data.append(i)
        return data

    def clear_file(self, filepath):
        with open(filepath, 'w+') as csvfile:
            obj1 = csv.writer(csvfile)

    def append_file(self, filepath, data):
        with open(filepath, 'a') as csvfile:
            newdata = csv.writer(csvfile)
            newdata.writerow(data)   
