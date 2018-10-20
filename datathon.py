import pandas as pd
import csv
import os
FILEDIR = "./processed"
class Datathon:
    def data_set_path(self, set_name):
        return os.path.join(FILEDIR,set_name+".csv")

    def print_info(self, ):
        print('data sets: ', self.data_set)
        self.df_array = {}
        for ds in self.data_set:
            df = pd.read_csv(self.data_set_path(ds))
            self.df_array[ds] = df
            print(df.head(5))

    def read_csv_file(self, ):
        with open(self.csv_filename) as csv_file:
            #seperate files and clean
            csv_reader = csv.reader(csv_file, delimiter=',')
            self.data_set = []
            data_set_name = ""
            feature_num = 0
            for row in csv_reader:
                if row[0]:
                    self.data_set.append(row[0])
                    data_set_name = row[0]
                    print("data set name: ",data_set_name)
                    feature_num = sum(map(lambda x: 1 if x else 0, row))-1
                    print("number of features: ", feature_num)
                    filepath = self.data_set_path(data_set_name)
                    print("open file ", filepath)
                    csv_file = open(filepath, mode='w')
                    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow(row[2:2+feature_num-1])
                else:
                    if any(row):
                        csv_writer.writerow(row[2:2+feature_num-1])
                    else:
                        csv_file.close()

            #print('data sets: ', data_set)


    def __init__(self, csv_filename):
        self.csv_filename = csv_filename
        self.read_csv_file()
        self.print_info()

if __name__ == '__main__':
    fname = "SoCal Datathon Data Table Heads.csv"
    D = Datathon(fname)
