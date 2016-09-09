import requests

#performs a simple post request using the python requests library
#url = url to an endpoint that accepts post requests
#data = request body. In the case of querying SSB it contains a json query
def execute_simple_post_query(url, query):
	return requests.post(url, data = query)

#performs a multipart/form request using the python requests library
#url = url to an endpoint that accepts post requests
#files = one or several files to be uploaded
#headers = requests headers
#data = various parameters that the endpoint may require
def multipart_post(url, files, headers, params):
	return requests.post(url, files = files, headers = headers, data = params)
