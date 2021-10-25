'''Module to view covid vaccinations from Public Health England
'''

from .connection import Connection
from enum import Enum

class ViewVaccinations():
    def __init__(self):
        pass

    class DateType(Enum):
        PUBLISH_DATE = 0
        VACCINATION_DATE = 1

    def viewVaccinations(self, areaType: str='nation', areaName: str = 'england',
            dateType: DateType = DateType.PUBLISH_DATE):
        conn = Connection()
        assert dateType in [ViewVaccinations.DateType.PUBLISH_DATE, ViewVaccinations.DateType.VACCINATION_DATE]
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date':'date',
            f'newPeopleVaccinatedCompleteBy{self.dateTypeMap[dateType]}Date':
                f'newPeopleVaccinatedCompleteBy{self.dateTypeMap[dateType]}Date',
            f'newPeopleVaccinatedFirstDoseBy{self.dateTypeMap[dateType]}Date':
                f'newPeopleVaccinatedFirstDoseBy{self.dateTypeMap[dateType]}Date',
            f'newPeopleVaccinatedSecondDoseBy{self.dateTypeMap[dateType]}Date':
                f'newPeopleVaccinatedSecondDoseBy{self.dateTypeMap[dateType]}Date',
            f'cumPeopleVaccinatedCompleteBy{self.dateTypeMap[dateType]}Date':
                f'cumPeopleVaccinatedCompleteBy{self.dateTypeMap[dateType]}Date',
            f'cumPeopleVaccinatedFirstDoseBy{self.dateTypeMap[dateType]}Date':
                f'cumPeopleVaccinatedFirstDoseBy{self.dateTypeMap[dateType]}Date',
            f'cumPeopleVaccinatedSecondDoseBy{self.dateTypeMap[dateType]}Date':
                f'cumPeopleVaccinatedSecondDoseBy{self.dateTypeMap[dateType]}Date'}))
    
    def viewNewVaccinations(self, areaType: str='nation', areaName: str='england',
            dateType: DateType = DateType.PUBLISH_DATE):
        conn = Connection()
        assert dateType in [ViewVaccinations.DateType.PUBLISH_DATE, ViewVaccinations.DateType.VACCINATION_DATE]
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date':'date',
            f'newPeopleVaccinatedCompleteBy{self.dateTypeMap[dateType]}Date':
                f'newPeopleVaccinatedCompleteBy{self.dateTypeMap[dateType]}Date',
            f'newPeopleVaccinatedFirstDoseBy{self.dateTypeMap[dateType]}Date':
                f'newPeopleVaccinatedFirstDoseBy{self.dateTypeMap[dateType]}Date',
            f'newPeopleVaccinatedSecondDoseBy{self.dateTypeMap[dateType]}Date':
                f'newPeopleVaccinatedSecondDoseBy{self.dateTypeMap[dateType]}Date'}))

    def viewCumVaccinations(self, areaType: str='nation', areaName: str = 'england',
            dateType: DateType = DateType.PUBLISH_DATE):
        conn = Connection()
        assert dateType in [ViewVaccinations.DateType.PUBLISH_DATE, ViewVaccinations.DateType.VACCINATION_DATE]
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date':'date',
            f'cumPeopleVaccinatedCompleteBy{self.dateTypeMap[dateType]}Date':
                f'cumPeopleVaccinatedCompleteBy{self.dateTypeMap[dateType]}Date',
            f'cumPeopleVaccinatedFirstDoseBy{self.dateTypeMap[dateType]}Date':
                f'cumPeopleVaccinatedFirstDoseBy{self.dateTypeMap[dateType]}Date',
            f'cumPeopleVaccinatedSecondDoseBy{self.dateTypeMap[dateType]}Date':
                f'cumPeopleVaccinatedSecondDoseBy{self.dateTypeMap[dateType]}Date',}))
        
    def viewVaccinationsByAge(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'vaccinationsAgeDemographics':'vaccinationsAgeDemographics'}))

    dateTypeMap = {
        DateType.PUBLISH_DATE: 'Publish',
        DateType.VACCINATION_DATE: 'Vaccination',
    }