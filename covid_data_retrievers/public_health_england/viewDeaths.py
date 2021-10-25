"""Module to retrieve covid death data from public health england.
"""

from .connection import Connection
from enum import Enum

class ViewDeaths():
    def __init__(self):
        pass

    class DateType(Enum):
        PUBLISH_DATE = 0
        DEATH_DATE = 1

    def viewDeaths(self, areaType: str='nation', areaName: str='england',
            dateType: DateType=DateType.PUBLISH_DATE):
        conn = Connection()
        assert dateType in [ViewDeaths.DateType.PUBLISH_DATE, ViewDeaths.DateType.DEATH_DATE], "Invalid Date Type"
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date', 
            f'newDeathsBy{self.dateTypeMap[dateType]}Date':
                f'newDeathsBy{self.dateTypeMap[dateType]}Date', 
            f'cumDeathsBy{self.dateTypeMap[dateType]}Date':
                f'cumDeathsBy{self.dateTypeMap[dateType]}Date'}))

    def viewDeathsByAge(self, areaType: str='nation', areaName: str = 'england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'areaName': 'areaName',
            'newDeaths28DaysByDeathDateAgeDemographics': 'newDeaths28DaysByDeathDateAgeDemographics'}))


    dateTypeMap = {
        DateType.PUBLISH_DATE: 'Publish',
        DateType.DEATH_DATE: 'Death'}
    
