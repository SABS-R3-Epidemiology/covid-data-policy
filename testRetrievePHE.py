import covid_data_retrievers as cvd
import covid_data_retrievers.public_health_england as phe
import json
from pprint import pprint


data = phe.ViewCases().viewCases()

json.dump(data, open('testData.json', 'w'), indent=4)
