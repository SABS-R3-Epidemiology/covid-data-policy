'''Module to retrieve covid tests data from Public Health England
'''

from .connection import Connection
from enum import Enum


class ViewTests():
    def __init__(self):
        pass

    def viewLFDTests(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'areaName': 'areaName',
            'newLFDTests': 'newLFDTests',
            'cumLFDTests':'cumLFDTests'}))

    def viewPCRTests(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'areaName': 'areaName',
            'newPCRTestsByPublishDate': 'newPCRTestsByPublishDate',
            'cumPCRTestsByPublishDate':'cumPCRTestsByPublishDate'}))
    
    def viewAntibodyTests(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'areaName': 'areaName',
            'newAntibodyTestsByPublishDate': 'newAntibodyTestsByPublishDate',
            'cumAntibodyTestsByPublishDate':'cumAntibodyTestsByPublishDate'}))

    def viewPillarOneTests(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'areaName': 'areaName',
            'newPillarOneTestsByPublishDate': 'newPillarOneTestsByPublishDate',
            'cumPillarOneTestsByPublishDate': 'cumPillarOneTestsByPublishDate',
            'capacityPillarOne': 'capacityPillarOne'}))

    def viewPillarTwoTests(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'areaName': 'areaName',
            'newPillarTwoTestsByPublishDate': 'newPillarTwoTestsByPublishDate',
            'cumPillarTwoTestsByPublishDate': 'cumPillarTwoTestsByPublishDate',
            'capacityPillarTwo': 'capacityPillarTwo'}))

    def viewPillarThreeTests(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'areaName': 'areaName',
            'newPillarThreeTestsByPublishDate': 'newPillarThreeTestsByPublishDate',
            'cumPillarThreeTestsByPublishDate': 'cumPillarThreeTestsByPublishDate',
            'capacityPillarThree': 'capacityPillarThree'}))

    def viewPillarFourTests(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'areaName': 'areaName',
            'newPillarFourTestsByPublishDate': 'newPillarFourTestsByPublishDate',
            'cumPillarFourTestsByPublishDate': 'cumPillarFourTestsByPublishDate',
            'capacityPillarFour': 'capacityPillarFour'}))

    def viewPillarOneTwoTests(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'areaName': 'areaName',
            'newPillarOneTwoTestsByPublishDate': 'newPillarOneTwoTestsByPublishDate',
            'cumPillarOneTwoTestsByPublishDate': 'cumPillarOneTwoTestsByPublishDate',
            'capacityPillarOneTwo': 'capacityPillarOneTwo'}))

    def viewPillarTests(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'areaName': 'areaName',
            'newPillarOneTestsByPublishDate': 'newPillarOneTestsByPublishDate',
            'cumPillarOneTestsByPublishDate': 'cumPillarOneTestsByPublishDate',
            'capacityPillarOne': 'capacityPillarOne',
            'newPillarTwoTestsByPublishDate': 'newPillarTwoTestsByPublishDate',
            'cumPillarTwoTestsByPublishDate': 'cumPillarTwoTestsByPublishDate',
            'capacityPillarTwo': 'capacityPillarTwo',
            'newPillarThreeTestsByPublishDate': 'newPillarThreeTestsByPublishDate',
            'cumPillarThreeTestsByPublishDate': 'cumPillarThreeTestsByPublishDate',
            'capacityPillarThree': 'capacityPillarThree',
            'newPillarFourTestsByPublishDate': 'newPillarFourTestsByPublishDate',
            'cumPillarFourTestsByPublishDate': 'cumPillarFourTestsByPublishDate',
            'capacityPillarFour': 'capacityPillarFour',
            'newPillarOneTwoTestsByPublishDate': 'newPillarOneTwoTestsByPublishDate',
            'cumPillarOneTwoTestsByPublishDate': 'cumPillarOneTwoTestsByPublishDate',
            'capacityPillarOneTwo': 'capacityPillarOneTwo'}))
    