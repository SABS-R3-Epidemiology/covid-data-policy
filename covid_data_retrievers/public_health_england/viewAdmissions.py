"""Module to retrieve covid admission data from public health england.
"""

from .connection import Connection
from enum import Enum

class ViewAdmissions():
    def __init__(self):
        pass

    def viewAdmissions(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'newAdmissions': 'newAdmissions',
            'cumAdmissions': 'cumAdmissions'}))
    
    def viewAdmissionsByAge(self, areaType: str='nation', areaName: str='england'):
        conn = Connection()
        return list(conn.get(conn.makeAreaFilter(areaType, areaName),
            {'date': 'date',
            'cumAdmissionsByAge': 'cumAdmissionsByAge'}))

    
