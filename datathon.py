import pandas as pd
import numpy as np
import plotly
import plotly.figure_factory as ff
import csv
import os
FILEDIR = "./data"
CHEMPROCDIR = "./data/chem_processed"
class Datathon:
    def data_set_path(self, set_name):
        return os.path.join(FILEDIR,set_name+".csv")

    def chem_proc_path(self, set_name):
        return os.path.join(CHEMPROCDIR,set_name+".csv")

    def get_chemicals_data(self, chemical, year):
        chemicals = self.df_dict["chemicals"]
        ch = chemicals.loc[chemicals["chemical_species"] == chemical]
        ch_y = ch.loc[ch["year"]==year]
        chemical_df = ch_y[["fips","value"]]
        return chemical_df

    def get_chem_processed_data(self, chemical, new_name):
        df = pd.read_csv(self.chem_proc_path(chemical),encoding = "ISO-8859-1")
        chemical_df = df[["fips","CL_score"]]
        chemical_df = chemical_df.rename(columns={'fips': 'fips', 'CL_score': new_name})
        return chemical_df

    def get_water_usage_by_fips(self, usage_type , fips, new_name):
        water_usage = self.df_dict["water_usage"]
        usage_filtered = water_usage.loc[map(lambda x: x in np.array(fips),list(water_usage["fips"]))]
        usage = usage_filtered[["fips",usage_type]]
        usage = usage.rename(columns={'fips': 'fips', usage_type: new_name})
        return usage

    def plot_chem_processed_data(self, chemical):
        df = pd.read_csv(self.chem_proc_path(chemical),encoding = "ISO-8859-1")
        chemical_df = df[["fips","CL_score"]]
        fig = ff.create_choropleth(fips=chemical_df["fips"], values=chemical_df["CL_score"])
        plotly.offline.iplot(fig, filename='')

    def read_data_files(self, ):
        print('data sets: ', self.data_set)
        for ds in self.data_set:
            print(ds)
            df = pd.read_csv(self.data_set_path(ds),encoding = "ISO-8859-1")
            self.df_dict[ds] = df


    def __init__(self,):
        self.data_set = ['chemicals', 'droughts', 'earnings', 'education_attainment', 'industry_occupation', 'water_usage']
        self.df_dict = {}
        #self.data_set = ['chemicals', 'droughts', 'industry_occupation', 'water_usage']
        #self.csv_filename = csv_filename
        #self.read_csv_file()
        self.read_data_files()

if __name__ == '__main__':
    D = Datathon()
