import pandas as pd

def execute_jobs(dict):
	df = pd.DataFrame(dict)
	df.to_csv("files/data.csv", index = False)
	return
