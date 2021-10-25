
from abc import ABC, abstractmethod
import pandas as pd
import pkg_resources

DATA_PATH = pkg_resources.resource_filename('covid_data_retrievers',
    'dataSources/covid19infectionsurveydatasets20211022england.xlsx')

class ONSData():
    def __init__(self):
        self.sourceFile = DATA_PATH
    
    def summaryPositivity(self):
        return pd.read_excel(self.sourceFile, sheet_name = 'UK summary - positivity',
            header=[0,1], skiprows=4, skipfooter=15)

    def summaryIncidence(self):
        return pd.read_excel(self.sourceFile, sheet_name = 'UK summary - incidence ',
            header = [0,1], skiprows=4, skipfooter=13)

    def dailyPositivityByRegion(self):
        return pd.read_excel(self.sourceFile, sheet_name = '1f',
            header=[0,1], skiprows=4, skipfooter=13)

    def dailyPositivityByAgeGroup(self):
        return pd.read_excel(self.sourceFile, sheet_name = '1h',
            header = [0,1], skiprows=4, skipfooter=12)

    def dailyPositivityByAge(self):
        return pd.read_excel(self.sourceFile, sheet_name = '1i',
            header = [0,1], skiprows=4, skipfooter = 9)

    def weighted14DayPositivityByAgeGroup(self):
        return pd.read_excel(self.sourceFile, sheet_name='1j',
            header=[0,1], skiprows=4, skipfooter=11)
