import requests
import json

class Connection:
    def __init__(self):
        self.endpoint = 'https://api.coronavirus.data.gov.uk/v1/data'

    def makeParams(self, filters: list, structure: dict, latestby: str=None, format: str=None, page: int=1):
        api_params = {
            "filters": str.join(";", filters),
            "structure": json.dumps(structure, separators=(",", ":")),
            "page": page
        }
        if latestby is not None: api_params["latestby"]=latestby
        if format is not None: api_params["format"] = format
        return api_params

    def makeAreaFilter(self, areaType: str='Nation', areaName: str='england'):
        assert areaType is not None, 'Area Type cannot be None'
        f = [f'areaType={areaType}']
        if areaName is not None: f.append(f'areaName={areaName}')
        return f

    def get(self, filters=['areaType=overview'],
            structure={'date': 'date', 'newCasesByPublishDate':'newCasesByPublishDate'},
            latestby=None, format=None, page=None):
        params = self.makeParams(filters, structure, latestby, format, 1)
        response = requests.get(self.endpoint, params=params, timeout=10)
        
        while response.status_code == 200:
            data = response.json()
            print('Performed Request')
            for row in data['data']:
                yield row

            if 'pagination' not in data:
                return
            if data['pagination']['next'] is None:
                return
            
            params['page'] += 1
            response = requests.get(self.endpoint, params=params, timeout=10)
        print(response.content)

