import requests
import json

def execute_query(query, url):
	r = requests.get(url)
	return r
