""" Class used to retrieve data from the ONS survey
Data is taken from the .xlsx file downloaded from
https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/datasets/coronaviruscovid19infectionsurveydata

Methods in the class are used to retrieve pandas DataFrames with the cleaned data
"""

from abc import ABC, abstractmethod
import pandas as pd
import pkg_resources

DATA_PATH = pkg_resources.resource_filename('covid_data_retrievers',
    'dataSources/covid19infectionsurveydatasets20211022england.xlsx')

class ONSData():
    def __init__(self):
        self.sourceFile = DATA_PATH
    
    def summaryPositivity(self):
        """Retrieve Estimated Positivity over time periods for
            England, Wales, Northern Ireland and Scotland
        
            Returned DataFrame is Multi-indexed

        : rtype: pd.DataFrame
        : returns: Pandas Dataframe with Positivity data over time
        """
        return pd.read_excel(self.sourceFile, sheet_name = 'UK summary - positivity',
            header=[0,1], skiprows=4, skipfooter=15)

    def summaryIncidence(self):
        """Retrieve Estimated Incidence over time periods for
            England, Wales, Northern Ireland and Scotland

            Returned DataFrame is Multi-indexed

        : rtype: pd.DataFrame
        : returns: Pandas Dataframe with Positivity data over time
        """
        return pd.read_excel(self.sourceFile, sheet_name = 'UK summary - incidence ',
            header = [0,1], skiprows=4, skipfooter=13)

    def dailyPositivityByRegion(self):
        """Retrieve Modelled Daliy Positivity Rate by Region
            
            Returned DataFrame is Multi-indexed
        
        : rtype: pd.DataFrame
        : returns: Pandas Dataframe with Modelled Positivity Rate grouped by Sub-Region
        """
        return pd.read_excel(self.sourceFile, sheet_name = '1f',
            header=[0,1], skiprows=4, skipfooter=13)

    def dailyPositivityByAgeGroup(self):
        """Retrieve Modelled Daliy Positivity Rate by Age Groups
            
            Returned DataFrame is Multi-indexed
        
        : rtype: pd.DataFrame
        : returns: Pandas Dataframe with Modelled Positivity Rate grouped by Age Groups
        """
        return pd.read_excel(self.sourceFile, sheet_name = '1h',
            header = [0,1], skiprows=4, skipfooter=12)

    def dailyPositivityByAge(self):
        """Retrieve Modelled Daliy Positivity Rate by Age
            
            Returned DataFrame is Multi-indexed
        
        : rtype: pd.DataFrame
        : returns: Pandas Dataframe with Modelled Positivity Rate grouped by Age
        """
        return pd.read_excel(self.sourceFile, sheet_name = '1i',
            header = [0,1], skiprows=4, skipfooter = 9)

    def weighted14DayPositivityByAgeGroup(self):
        """Retrieve Non-Overlapping 14-day weighted Positivity Estimates by Age Groups
            
            Returned DataFrame is Multi-indexed
        
        : rtype: pd.DataFrame
        : returns: Pandas Dataframe with Estimated Positivity Rate grouped by Age Group
        """
        return pd.read_excel(self.sourceFile, sheet_name='1j',
            header=[0,1], skiprows=4, skipfooter=11)
