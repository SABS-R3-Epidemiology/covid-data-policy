"""Module to retrieve covid case data from public health england.
"""

from .connection import Connection
from enum import Enum

class ViewCases():
    def __init__(self):
        pass

    class DateType(Enum):
        PUBLISH_DATE = 0
        SPECIMEN_DATE = 1
        DEATH_DATE = 2

    def viewCases(self, areaType: str='nation', areaName: str='england',
            dateType: DateType=DateType.PUBLISH_DATE):
        conn = Connection()
        assert dateType in [ViewCases.DateType.PUBLISH_DATE, ViewCases.DateType.SPECIMEN_DATE], "Invalid Date Type"
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'areaName': 'areaName',
            f'newCasesBy{self.dateTypeMap[dateType]}Date':
                f'newCasesBy{self.dateTypeMap[dateType]}Date',
            f'cumCasesBy{self.dateTypeMap[dateType]}Date':
                f'cumCasesBy{self.dateTypeMap[dateType]}Date'}))

    def viewCasesByAge(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'areaName': 'areaName',
            'newCasesBySpecimenDateAgeDemographics': 'newCasesBySpecimenDateAgeDemographics'}))

    def viewAlertLevel(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'areaName': 'areaName',
            'alertLevel': 'alertLevel'}))

    dateTypeMap = {
        DateType.PUBLISH_DATE: 'Publish',
        DateType.SPECIMEN_DATE: 'Specimen'}
    
