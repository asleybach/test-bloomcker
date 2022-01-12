import pandas as pd
import requests
import json

def execute_jobs():
	r = requests.get('https://covid19-api.com/country/all?format=json')
	data = json.loads(r.text)
	df = pd.DataFrame(data)
	df = df.drop(['code','latitude', 'longitude', 'lastChange', 'lastUpdate'], axis = 1)
	df.to_csv("files/data.csv", index = False)
	return
